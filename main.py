# main.py
import json
import os
import subprocess
from strands import Agent, tool
from strands.models.openai import OpenAIModel

@tool
def validate_syntax(code_string: str) -> str:
    temp_file = "_temp_check.py"
    with open(temp_file, "w") as f:
        f.write(code_string)
    try:
        subprocess.run(["python3", "-m", "py_compile", temp_file], check=True, capture_output=True, text=True)
        return "SUCCESS: Code syntax is valid."
    except subprocess.CalledProcessError as e:
        return f"CRITICAL SYNTAX ERROR DETECTED:\n{e.stderr}"
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

model = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENROUTER_API_KEY", ""),
        "base_url": "https://openrouter.ai/api/v1"
    },
    model_id="openrouter/free"
)

autonomous_agent = Agent(
    model=model,
    tools=[validate_syntax],
        system_prompt=(
        "You are ZeroToggle, an autonomous software refactoring engine.\n"
        "Your task is to wrap existing functions in the source code with dynamic feature flags.\n\n"
        "CRITICAL RULES FOR FALLBACK STATEMENTS:\n"
        "When a flag is disabled, you MUST look at the function's return type hint (e.g., -> list, -> bool) and match it EXACTLY using this matrix:\n"
        "- If the function ends in `-> str` : return \"\"\n"
        "- If the function ends in `-> int` : return 0\n"
        "- If the function ends in `-> float` : return 0.0\n"
        "- If the function ends in `-> bool` : return False\n"
        "- If the function ends in `-> list` : return []\n"
        "- If the function ends in `-> dict` : return {}\n"
        "- If the function has NO type hint, or ends in `-> None` : return None\n"
        "NEVER use a blanket `return \"\"` for functions that do not return strings.\n\n"
        "GENERAL RULES:\n"
        "1. Include `from flags_helper import get_flag` at the very top of the generated code.\n"
        "2. DO NOT invent new logic or features. Only wrap existing logic inside `if get_flag('FlagName'):` checks.\n"
        "3. Generate PascalCase flag names based on function names.\n"
        "4. You MUST call `validate_syntax` on your refactored code before finalizing.\n"
        "5. Output ONLY raw JSON strictly adhering to this structure (no markdown fences):\n"
        "{\n"
        '  "detected_flags": ["<FLAG_NAME_1>", "<FLAG_NAME_2>"],\n'
        '  "refactored_code": "<FULL_REFACTORED_CODE_STRING>"\n'
        "}\n"
    )

)

def run_zero_toggle(source_code: str) -> dict:
    prompt = f"Analyze this clean Python source code, add the import, wrap functions in get_flag checks, and validate syntax:\n\n{source_code}"
    response = autonomous_agent(prompt)
    output_text = str(response).strip()
    cleaned_output = output_text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    result = json.loads(cleaned_output)

    with open("refactored_app.py", "w") as f:
        f.write(result["refactored_code"])

    return result
