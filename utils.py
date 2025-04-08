# utils.py
import json
import traceback

def log_error(error):
    print(f"[❌ ERROR] {str(error)}")
    traceback.print_exc()

def log_info(message):
    print(f"[ℹ️ INFO] {message}")

def pretty_print(title, content):
    print(f"\n=== {title} ===")
    print(json.dumps(content, indent=2))
