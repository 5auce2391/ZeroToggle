# flags_helper.py
import json
import os

def get_flag(flag_name: str) -> bool:
    """Reads feature flags live from the shared JSON file."""
    if os.path.exists("flags.json"):
        with open("flags.json", "r") as f:
            try:
                flags = json.load(f)
                return flags.get(flag_name, False)
            except json.JSONDecodeError:
                return False
    return False
