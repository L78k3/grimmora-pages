import json
import urllib.request
import urllib.error
import yaml
from pathlib import Path

def load_config(config_path: str = "automation/config.yaml") -> dict:
    path = Path(config_path)
    if path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return {}

class OllamaClient:
    def __init__(self, config_path: str = "automation/config.yaml"):
        config = load_config(config_path)
        ollama_cfg = config.get("ollama", {})
        
        self.host = ollama_cfg.get("host", "http://100.85.13.99:11434").rstrip("/")
        self.primary_model = ollama_cfg.get("model", "llama3.1:8b-instruct-q4_K_M")
        self.fallback_model = ollama_cfg.get("fallback_model", "qwen2.5:14b-instruct-q4_K_M")
        self.timeout = ollama_cfg.get("timeout_seconds", 120)
        
        ha_cfg = config.get("home_assistant", {})
        self.ha_webhook_url = ha_cfg.get("webhook_url", "")
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "GrimmoraVaultBot/1.0"
        }

    def check_health(self) -> bool:
        """Checks if Ollama host is reachable over Tailscale."""
        try:
            req = urllib.request.Request(f"{self.host}/api/tags", headers={"User-Agent": self.headers["User-Agent"]}, method="GET")
            with urllib.request.urlopen(req, timeout=5) as resp:
                return resp.status == 200
        except Exception:
            return False

    def notify_home_assistant(self, filename: str) -> bool:
        """Sends a POST to Home Assistant webhook to trigger a mobile push notification."""
        if not self.ha_webhook_url:
            print("⚠️ Home Assistant webhook URL not configured.")
            return False

        payload = json.dumps({
            "message": f"Ollama job waiting for processing: {filename}",
            "filename": filename,
            "status": "pending_ollama"
        }).encode("utf-8")

        req = urllib.request.Request(
            self.ha_webhook_url,
            data=payload,
            headers=self.headers,
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"📲 Home Assistant notification triggered successfully (HTTP {resp.status}).")
                return resp.status in (200, 201, 204)
        except urllib.error.HTTPError as e:
            print(f"⚠️ Failed to notify Home Assistant: HTTP Error {e.code}: {e.reason}")
            # HA returns 405 Method Not Allowed or 400/404 if the webhook isn't configured yet
            if e.code in (405, 400, 404, 403):
                print("   (This usually means the webhook ID 'ollama_job_waiting' needs to be created in HA!)")
            return False
        except Exception as e:
            print(f"⚠️ Failed to notify Home Assistant: {e}")
            return False

    def generate(self, prompt: str, system: str = "", model: str = None) -> str:
        """
        Sends a generation request to Ollama.
        Tries primary model first, falling back to secondary model if primary fails.
        """
        target_model = model or self.primary_model
        url = f"{self.host}/api/generate"
        
        payload_data = {
            "model": target_model,
            "prompt": prompt,
            "system": system,
            "stream": False
        }
        payload = json.dumps(payload_data).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=self.headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("response", "")
        except Exception as e:
            if target_model != self.fallback_model:
                print(f"⚠️ Primary model '{target_model}' failed ({e}). Retrying with fallback '{self.fallback_model}'...")
                return self.generate(prompt, system=system, model=self.fallback_model)
            raise RuntimeError(f"Ollama API request failed on all models: {e}")

if __name__ == "__main__":
    client = OllamaClient()
    print(f"Checking Ollama status at {client.host}...")
    is_online = client.check_health()
    print(f"Ollama Online: {is_online}")

    if is_online:
        print("Testing basic generation...")
        try:
            resp = client.generate("Say 'Ollama is online and operational!' in 5 words or less.")
            print(f"Response: {resp.strip()}")
        except Exception as err:
            print(f"Generation error: {err}")
    else:
        print("Desktop PC appears to be offline or unreachable over Tailscale.")
        print("Testing Home Assistant notification payload...")
        client.notify_home_assistant("Test_Entry_45.docx")