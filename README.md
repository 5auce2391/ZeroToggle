# ⚡ ZeroToggle:-

### Autonomous AI Refactoring & Real-Time Feature Flag Engine:-

ZeroToggle is an autonomous AI-powered refactoring and real-time feature flag engine built with Strands Agents.

It automates the tedious and error-prone process of retrofitting traditional Python codebases with dynamic feature flags—without requiring developers to manually wrap code blocks, write fallback logic, or build custom control panels.

> Note: ZeroToggle is currently a barebones demonstration prototype designed to showcase the concept of autonomous AI-driven feature-flag refactoring. It is intended for experimentation, demonstrations, and proof-of-concept purposes rather than production use.

---

## 🚀 Overview:-

Feature flags are powerful, but introducing them into an existing application can quickly lead to boilerplate, nested conditionals, and maintenance overhead.

ZeroToggle takes a different approach.

It starts with a clean, immutable source file, uses an AI agent to intelligently identify and refactor feature-worthy code paths, validates the generated Python syntax in a sandboxed environment, and produces a live feature-flagged version of the application.

The resulting feature flags can then be controlled in real time through a Streamlit dashboard while a separate consumer application reflects those changes instantly.

### The Core Idea

```Clean Source Code
       │
       ▼
┌──────────────────────┐
│   Strands AI Agent   │
│  Autonomous Refactor │
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
       ↙     ↘
      ▼       ▼
 Dashboard   Consumer App
  :8501        :8502
```
# 💡 Problem:-
Adding feature flags to an existing application typically requires developers to manually:

Identify code paths that should be configurable.
Wrap existing logic with feature-flag checks.
Implement fallback behavior.
Maintain flag state.
Build or configure a control interface.
Test the resulting changes for syntax and runtime issues.
For larger codebases, this process becomes repetitive, time-consuming, and prone to human error.

It can also pollute otherwise clean application logic with excessive conditional code.

# ✨ Solution:-
ZeroToggle automates this workflow using an AI agent.

## The system:-
Takes the original application source code.
Uses a Strands Agent to analyze and refactor the code.
Injects dynamic get_flag() hooks into appropriate code paths.
Validates the generated code using a sandboxed Python syntax-validation tool.
Writes the resulting feature-flagged application.
Stores live feature-flag state in flags.json.
Allows developers to control flags through a Streamlit dashboard.
Reflects flag changes in the running consumer application without requiring a restart.
The original app_code.py remains untouched.

# 🏗️ Architecture:-
ZeroToggle consists of several lightweight components working together:

# File Purpose:-
app_code.py - Original, immutable application source with no feature flags
main.py - Strands autonomous AI agent responsible for refactoring
refactored_app.py - AI-generated application containing dynamic feature-flag hooks
flags_helper.py -  Backend bridge that reads the current state from flags.json
flags.json - Persistent source of live feature-flag state
dashboard.py - Streamlit control plane running on port 8501
app_web.py - Standalone consumer application running on port 8502

# Component Flow:-
                    ┌─────────────────┐
                    │   app_code.py   │
                    │  Original Code  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     main.py     │
                    │  Strands Agent  │
                    │                 │
                    │ OpenRouter LLM  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Syntax Validator│
                    │    Sandbox      │
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
                 ┌──────────┘ └──────────┐
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │  dashboard.py   │     │   app_web.py    │
        │    Port 8501    │     │    Port 8502     │
        │                 │     │                 │
        │ Control Plane   │     │ Consumer App    │
        └─────────────────┘     └─────────────────┘

# 🤖 AI Refactoring Workflow:-
The autonomous refactoring process is handled by main.py.

The Strands Agent is equipped with a syntax-validation capability that helps ensure generated code is structurally valid before it is used.

Refactoring Pipeline
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

This allows the original application source to remain clean while the AI-generated version becomes the feature-flagged runtime implementation.

# 🎛️ Real-Time Feature Flags
Feature-flag state is maintained through flags.json.

The lightweight flags_helper.py module acts as the bridge between the running application and the current flag state.

Conceptually:

if get_flag("some_feature"):
    # New behavior
else:
    # Existing behavior

This allows the consumer application to react to changes in feature-flag state without requiring a server restart.

# 🖥️ Dashboard
The ZeroToggle control plane is implemented using Streamlit.

The dashboard provides the interface for:

Triggering the autonomous AI refactoring process.
Viewing generated feature flags.
Enabling or disabling flags.
Managing live feature-flag state.
The dashboard runs on:

http://localhost:8501

# 🌐 Consumer Application
app_web.py is a standalone Streamlit application that consumes the refactored module.

It runs independently from the control dashboard on port 8502.

http://localhost:8502

This makes it possible to keep the dashboard and application open side-by-side and observe feature-flag changes in real time.

# 🛠️ Installation:- 

## Prerequisites:

Python 3.x
pip
OpenRouter API key

1. Clone the Repository
git clone https://github.com/your-username/zerotoggle.git
cd zerotoggle

2. Install Dependencies
pip install streamlit strands-sdk

3. Configure OpenRouter
ZeroToggle uses an OpenRouter API key for the AI-powered refactoring workflow.

## macOS / Linux
export OPENROUTER_API_KEY="your-openrouter-api-key-here"

## Windows PowerShell
$env:OPENROUTER_API_KEY="your-openrouter-api-key-here"

Security: Never commit your API key to source control. For production deployments, use environment variables or a secure secrets manager.

# ▶️ Running ZeroToggle
ZeroToggle uses two Streamlit processes:

Dashboard / Control Plane: Port 8501
Consumer Application: Port 8502

### Terminal 1 — Start the Dashboard
streamlit run dashboard.py

Then open
http://localhost:8501

### Terminal 2 — Start the Consumer App
streamlit run app_web.py --server.port 8502

### Then open:
http://localhost:8502

Keep both applications open side-by-side to test real-time feature-flag changes.

# 🔄 Typical Usage
A typical ZeroToggle session looks like this:

## Step 1 — Start with Clean Code 

Your original logic lives in:-
app_code.py

No feature flags or toggle-specific boilerplate are required.

## Step 2 — Run the AI Refactor

From the dashboard, trigger:-

 🚀 Run Autonomous AI Refactor:
The Strands Agent analyzes the source and generates the refactored implementation.

## Step 3 — Validate the Generated Code
The generated Python code is passed through the syntax-validation tool before being used.

## Step 4 — Manage Feature Flags
The dashboard exposes the generated toggles and allows you to change their state.

## Step 5 — Observe Live Behavior
The application running on port 8502 reads the current state and executes the corresponding code path.

No application restart is required for testing live flag changes (only occasional refreshing needed when required).

📁 Project Structure
zerotoggle/
│
├── app_code.py
│   └── Original immutable application logic
│
├── main.py
│   └── Strands AI autonomous refactoring agent
│
├── refactored_app.py
│   └── AI-generated feature-flagged application
│
├── flags_helper.py
│   └── Feature-flag state bridge
│
├── flags.json
│   └── Live feature-flag state
│
├── dashboard.py
│   └── Streamlit control plane (:8501)
│
├── app_web.py
│   └── Standalone consumer application (:8502)
│
└── README.md
    └── Project documentation

# 🧩 Key Technologies
Technology	Role
Python	Core application language
Strands Agents	Autonomous AI agent framework
OpenRouter	LLM provider
Streamlit	Dashboard and consumer UI
Feature Flags	Dynamic runtime behavior control

# 🔐 Design Principles
Immutable Source
The original app_code.py remains clean and untouched.

AI-Driven Refactoring
Developers don't need to manually retrofit every code path with feature-flag logic.

Validation Before Execution
Generated code is syntax-validated before becoming the live refactored implementation.

Separation of Concerns
The original source, AI-generated implementation, flag state, dashboard, and consumer application are separated into dedicated components.

Real-Time Control
Feature-flag state can be changed independently of the consumer application.

🧪 Development & Testing
For local development, run both applications simultaneously:

# Terminal 1
streamlit run dashboard.py

# Terminal 2
streamlit run app_web.py --server.port 8502

Then:
Open the dashboard on 8501.
Open the consumer application on 8502.
Run the autonomous AI refactor.
Enable and disable generated feature flags.
Observe the consumer application's behavior.

# 🧹 Port Cleanup
If ports 8501 or 8502 remain occupied after previous sessions, terminate the existing processes.

## macOS / Linux:
kill -9 $(lsof -t -i:8501,8502) 2>/dev/null || true

## Windows PowerShell
Stop-Process -Name python -Force -ErrorAction SilentlyContinue

Note: The Windows command terminates Python processes broadly. If you have other Python applications running, stop the specific process instead.

# ⚠️ Prototype Limitations
ZeroToggle is currently a barebones demonstration prototype and should be viewed primarily as a proof of concept.

The current implementation demonstrates the fundamental idea of using an autonomous AI agent to retrofit feature flags into an existing codebase, but significant development is required before the system could be considered production-ready.

## In particular:-

The AI model's code reasoning and refactoring capabilities require further improvement.
AI-generated modifications may not always be optimal or semantically correct.
Syntax validation alone does not guarantee behavioral correctness.
Complex codebases and advanced Python patterns may require additional model intelligence and validation.
The current feature-flag storage mechanism is intentionally lightweight.
Production-grade authentication, authorization, persistence, observability, and concurrency controls are not yet implemented.
AI-generated code should be reviewed and tested before being used in a production environment.
The project is therefore best suited for experimentation, research, demonstrations, and exploring the concept of autonomous code refactoring.

# 🗺️ Future Improvements:-

## 🤖 AI & Refactoring Intelligence
Improve the underlying AI model's code-understanding and reasoning capabilities.
Improve the accuracy of identifying suitable feature-flag insertion points.
Increase the reliability and quality of AI-generated refactored code.
Reduce unnecessary or overly aggressive source-code modifications.
Improve handling of complex control flow, nested functions, classes, decorators, async code, and external dependencies.
Introduce semantic and behavioral validation beyond basic syntax compilation.
Add automated test generation and execution after refactoring.
Explore specialized or fine-tuned models optimized for code transformation and feature-flag insertion.
Improve the agent's ability to understand larger, multi-file codebases.
Introduce iterative AI review, where generated refactors are analyzed and improved before being finalized.

## 🛡️ Safety & Reliability
Stronger sandboxing for AI-generated code.
Static analysis and security scanning.
Automated regression testing.
Runtime error monitoring and observability.
Automatic rollback of problematic refactors.
Human approval workflows before AI-generated changes reach production.
Git-based diff generation and review before applying changes.
Behavioral verification to ensure refactored code preserves the original application's expected behavior.

## 🏗️ Platform & Architecture
Persistent database-backed feature flags.
Production-grade distributed flag synchronization.
Multi-application and multi-environment flag management.
Feature-flag audit history and change tracking.
User authentication and role-based access control.
Percentage-based and gradual feature rollouts.
User, tenant, or environment-based targeting.
Scheduled feature-flag activation and expiration.

## 🔄 Developer Experience
CI/CD integration for automated AI refactoring.
IDE/editor integrations.
Visual code-diff previews before applying a refactor.
Better explanations of why the AI introduced each feature flag.
Configurable AI refactoring strategies and rules.
One-click rollback to the original implementation.
Improved dashboard UX for managing large numbers of feature flags.

## 🚀 Long-Term Vision:-
The long-term vision for ZeroToggle is to evolve from a barebones demonstration prototype into a reliable AI-assisted code transformation platform.
The goal is to allow developers to provide an existing application and have an AI agent safely:
```
Analyze
   ↓
Understand
   ↓
Identify Feature Boundaries
   ↓
Refactor
   ↓
Validate
   ↓
Test
   ↓
Review
   ↓
Deploy
   ↓
Manage Feature Flags
```
Achieving this vision will require substantial improvements across AI model intelligence, code transformation accuracy, semantic validation, automated testing, security, persistence, observability, and production architecture.

# 📄 License:-
This project is licensed under the terms of the MIT License.

