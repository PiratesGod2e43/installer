# Implementation plan

1. **Foundation:** PostgreSQL migrations, authentication, secure sessions, email verification/reset, MFA, CSRF, rate limits, RBAC enforcement, audit logs and tests.
2. **Node control plane:** short-lived credentials/mTLS, rotation/revocation, signed typed jobs, expiry, idempotency, replay protection and least-privilege agent. Never expose Docker/libvirt sockets.
3. **Minecraft:** pinned allowlisted images, isolated containers, CPU/RAM/disk/process/port quotas, lifecycle, console, scoped file access, backups and restore. Plugin/mod catalog must use allowlists/checksums.
4. **KVM VPS:** dedicated compute nodes with KVM enabled, private libvirt management, verified cloud images, cloud-init, tenant network isolation, quotas, console, snapshots and tested recovery.
5. **Billing:** plans and entitlements, invoice ledger, hosted checkout, signed/deduplicated webhooks, retries and reconciliation. QR only via a provider that officially supports it. Never trust screenshots/redirects as payment proof.
6. **Owner and roles:** branding (name/logo/favicon/colors/links/domain), Owner/Admin/Billing/Support/Moderator/User roles, server-side permissions, re-authentication for destructive actions and audit events.
7. **Operations:** monitoring, alerting, backup/restore, signed releases, migration dry runs, backup-before-update, health checks and rollback.

## Safety gates
- No shared database, directory, Docker network, service name or port with Pterodactyl.
- Detect port conflicts and stop rather than overwrite.
- Do not automatically stop/reconfigure existing services.
- Require confirmation for firewall/network changes.
- KVM requires host/provider virtualization support.
- "Unlimited" plans remain bounded by actual physical capacity and fair-use limits.
