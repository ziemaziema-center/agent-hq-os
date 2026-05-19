# Agent HQ OS Demo Workspace

This is a runnable, local-only demo of the Agent HQ OS workflow. It does not call APIs, send messages, publish posts, trade, or use real credentials.

## Try It

```bash
python setup_demo_workspace.py
```

On Windows you can also run:

```bat
bootstrap_project.bat
```

On macOS/Linux:

```bash
./bootstrap_project.sh
```

## What It Demonstrates

- A project boots from local instructions.
- Known failures and validated patterns are read before work.
- A task defines validation before execution.
- Telemetry is written after the task.

