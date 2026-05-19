# Install Guide

## Local Folder Install

```bash
mkdir -p agent_hq/{memory,telemetry,templates,docs}
cp starter_kit/project_bootstrap/* agent_hq/
```

## Repo-root Install

Place `AGENTS.md`, `CLAUDE.md`, and `SESSION_BOOT.md` in the repository root when your tools read root-level instructions.

## Team Install

Keep shared templates in version control and keep sensitive telemetry or private execution logs in a private folder. Public repos should include examples and blank templates, not private run history.

