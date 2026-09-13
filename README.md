# ⚡ ZeroToggle

### Autonomous AI Refactoring & Real-Time Feature Flag Engine

ZeroToggle is an autonomous AI-powered refactoring and real-time feature flag engine built with **Strands Agents**. It automates the tedious and error-prone process of retrofitting traditional Python codebases with dynamic feature flags—without requiring developers to manually wrap code blocks, write fallback logic, or build custom control panels.

> **Note:** ZeroToggle is currently a barebones demonstration prototype designed to showcase the concept of autonomous AI-driven feature-flag refactoring. It is intended for experimentation, demonstrations, and proof-of-concept purposes rather than production use.

---

## 🚀 Overview

Feature flags are powerful, but introducing them into an existing application can quickly lead to boilerplate, nested conditionals, and maintenance overhead. ZeroToggle takes a different approach by starting with a clean, immutable source file, using an AI agent to intelligently identify and refactor feature-worthy code paths, validating the generated Python syntax in a sandboxed environment, and producing a live feature-flagged version of the application.

The resulting feature flags can then be controlled in real time through a Streamlit dashboard while a separate consumer application reflects those changes instantly.

### The Core Idea

```text
Clean Source Code
        │
        ▼
┌──────────────────────┐
│    Strands AI Agent  │
│ Autonomous Refactor  │
└──────────┬───────────┘
           │
           ▼
   Syntax Validation
           │
           ▼
┌──────────────────────┐
│ refactored_app.py    │
│ Dynamic Flag Hooks   │
└──────────┬───────────┘
           │
           ▼
     flags.json
        ↙       ↘
      ▼           ▼
  Dashboard    Consumer App
    :8501         :8502

```

---

## 💡 The Problem

Adding feature flags to an existing application typically requires developers to manually:

* Identify code paths that should be configurable.
* Wrap existing logic with feature-flag checks.
* Implement fallback behavior and maintain flag state.
* Build or configure a control interface.
* Test resulting changes for syntax and runtime issues.

For larger codebases, this process becomes repetitive, time-consuming, and prone to human error, often polluting otherwise clean application logic with excessive conditional code.

---

## ✨ The Solution

ZeroToggle automates this workflow using an AI agent. The system performs the following sequence:

1. Takes the original application source code.
2. Uses a Strands Agent to analyze and refactor the code.
3. Injects dynamic `get_flag()` hooks into appropriate code paths.
4. Validates the generated code using a sandboxed Python syntax-validation tool.
5. Writes the resulting feature-flagged application.
6. Stores live feature-flag state in `flags.json`.
7. Allows developers to control flags through a Streamlit dashboard, reflecting changes in the running consumer application without a restart while leaving the original `app_code.py` untouched.

---

## 🏗️ Architecture & Component Flow

```text
                 ┌─────────────────┐
                 │   app_code.py   │
                 │ Original Code   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     main.py     │
                 │ Strands Agent   │
                 │                 │
                 │ OpenRouter LLM  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Syntax Validator│
                 │     Sandbox     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌──────────────────────┐
                 │ refactored_app.py    │
                 │ get_flag() Hooks     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌─────────────────┐
                 │   flags.json    │
                 │   Live State    │
                 └───────┬─┬───────┘
                         │ │
                ┌────────┘ └──────────┐
                ▼                     ▼
        ┌─────────────────┐   ┌─────────────────┐
        │  dashboard.py   │   │   app_web.py    │
        │    Port 8501    │   │    Port 8502    │
        │                 │   │                 │
        │ Control Plane   │   │ Consumer App    │
        └─────────────────>   └─────────────────┘

```

### File Purposes

| File | Purpose |
| --- | --- |
| `app_code.py` | Original, immutable application source with no feature flags |
| `main.py` | Strands autonomous AI agent responsible for refactoring |
| `refactored_app.py` | AI-generated application containing dynamic feature-flag hooks |
| `flags_helper.py` | Backend bridge that reads the current state from `flags.json` |
| `flags.json` | Persistent source of live feature-flag state |
| `dashboard.py` | Streamlit control plane running on port 8501 |
| `app_web.py` | Standalone consumer application running on port 8502 |

---

## 🤖 AI Refactoring Pipeline

The autonomous refactoring process is handled by `main.py`, equipped with a syntax-validation capability to ensure generated code is structurally valid before use.

```text
1. Read original source
         │
         ▼
2. AI analyzes application
         │
         ▼
3. Identify feature-worthy logic
         │
         ▼
4. Inject get_flag() hooks
         │
         ▼
5. Validate generated Python
         │
         ▼
6. Generate refactored_app.py

```

---

## 🎛️ Real-Time Feature Flags

Feature-flag state is maintained through `flags.json`. The lightweight `flags_helper.py` module acts as the bridge between the running application and the current flag state:

```python
if get_flag("some_feature"):
    # New behavior
else:
    # Existing behavior

```

This allows the consumer application to react to changes in feature-flag state without requiring a server restart.

* **Dashboard (`http://localhost:8501`):** Streamlit control plane for triggering refactors, viewing feature flags, and managing live states.
* **Consumer App (`http://localhost:8502`):** Standalone Streamlit application running independently to observe real-time feature updates side-by-side.

---

## 🛠️ Installation

### Prerequisites

* Python 3.x
* `pip`
* OpenRouter API key

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zerotoggle.git
cd zerotoggle

```

### 2. Install Dependencies

```bash
pip install streamlit strands-sdk

```

### 3. Configure OpenRouter

ZeroToggle uses an OpenRouter API key for the AI-powered refactoring workflow.

**macOS / Linux**

```bash
export OPENROUTER_API_KEY="your-openrouter-api-key-here"

```

**Windows PowerShell**

```powershell
$env:OPENROUTER_API_KEY="your-openrouter-api-key-here"

```

> **Security:** Never commit your API key to source control. For production deployments, use environment variables or a secure secrets manager.

---

## ▶️ Running ZeroToggle

ZeroToggle uses two concurrent Streamlit processes:

### Terminal 1 — Start the Dashboard

```bash
streamlit run dashboard.py

```

*(Open http://localhost:8501)*

### Terminal 2 — Start the Consumer App

```bash
streamlit run app_web.py --server.port 8502

```

*(Open http://localhost:8502)*

Keep both applications open side-by-side to test real-time feature-flag changes.

---

## 🔄 Typical Usage

1. **Start with Clean Code:** Your original logic lives in `app_code.py` with no feature flags or boilerplate.
2. **Run the AI Refactor:** From the dashboard (`:8501`), trigger the autonomous refactor. The Strands Agent analyzes the source and generates the implementation.
3. **Validate Generated Code:** The output is automatically passed through a syntax-validation sandbox.
4. **Manage Feature Flags:** Toggle flag states on the dashboard control plane.
5. **Observe Live Behavior:** The application on port 8502 reads the updated state instantly.

---

## 📁 Project Structure

```text
zerotoggle/
├── app_code.py         # Original immutable application logic
├── main.py             # Strands AI autonomous refactoring agent
├── refactored_app.py   # AI-generated feature-flagged application
├── flags_helper.py     # Feature-flag state bridge
├── flags.json          # Live feature-flag state
├── dashboard.py        # Streamlit control plane (:8501)
├── app_web.py          # Standalone consumer application (:8502)
└── README.md           # Project documentation

```

---

## 🧩 Key Technologies

| Technology | Role |
| --- | --- |
| **Python** | Core application language |
| **Strands Agents** | Autonomous AI agent framework |
| **OpenRouter** | LLM provider |
| **Streamlit** | Dashboard and consumer UI |
| **Feature Flags** | Dynamic runtime behavior control |

---

## 🧹 Port Cleanup

If ports 8501 or 8502 remain occupied after previous sessions:

**macOS / Linux**

```bash
kill -9 $(lsof -t -i:8501,8502) 2>/dev/null || true

```

**Windows PowerShell**

```powershell
Stop-Process -Name python -Force -ErrorAction SilentlyContinue

```

*(Note: The Windows command terminates Python processes broadly. Stop specific processes if running multiple apps.)*

---

## ⚠️ Prototype Limitations

ZeroToggle is a proof-of-concept demonstration prototype. Significant development is required for production readiness:

* The AI model's code reasoning requires further tuning; AI-generated modifications may occasionally be sub-optimal or semantically incorrect.
* Syntax validation alone does not guarantee behavioral correctness.
* Persistence, authentication, authorization, observability, and concurrency controls are intentionally lightweight.

---

## 🗺️ Future Improvements

* **AI & Refactoring Intelligence:** Enhance multi-file codebases handling, semantic validation, automated test generation, and complex control-flow handling.
* **Safety & Reliability:** Stronger sandboxing, static analysis, automated regression testing, and automatic rollbacks.
* **Platform & Architecture:** Database-backed feature flags, distributed synchronization, RBAC, and percentage-based progressive rollouts.
* **Developer Experience:** CI/CD pipeline integration, IDE extensions, and visual code-diff previews.

---

## 📄 License

This project is licensed under the terms of the [MIT License](https://www.google.com/search?q=LICENSE).
