# PiratesNodes — Independent Hosting Platform Starter

Standalone control-plane starter for Minecraft hosting and KVM VPS hosting. It does not install, modify, migrate, or depend on Pterodactyl.

**Honest status:** this is a starter codebase, not a complete production hosting platform. Authentication, database persistence, node agent, Minecraft/KVM provisioning, billing, payment gateway, Discord integration, backups and production deployment are not implemented. Provisioning flags default off. Do not expose this starter publicly.

## Local development
Requires Python 3.11+.
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Check `http://127.0.0.1:8000/health`. Development only.

## Configuration
```bash
cp .env.example .env
chmod 600 .env
```
Edit placeholders before running scripts. Never commit `.env`.

## Safety
`scripts/install.sh` is preflight-only; it does not install packages or change services/firewalls. `scripts/install-node.sh` and `scripts/update.sh` are disabled placeholders. See `docs/FEATURE_STATUS.md`, `docs/IMPLEMENTATION_PLAN.md`, and `docs/SECURITY.md`.
