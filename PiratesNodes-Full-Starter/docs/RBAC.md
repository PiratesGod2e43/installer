# RBAC proposal (not yet implemented)

| Capability | Owner | Admin | Billing | Support | Moderator | User |
|---|---|---|---|---|---|---|
| Brand/domain configuration | Yes | No by default | No | No | No | No |
| Role management | Yes | Delegated only | No | No | No | No |
| Node management | Yes | Yes | No | Health read-only | No | No |
| Invoice management | Yes | Read-only default | Yes | Limited read | No | Own invoices |
| Own-service management | Yes | Yes | No | Limited workflow | No | Within plan |
| Suspend/unsuspend | Yes | Audited | Billing workflow | Request only | No | No |
| Moderation | Yes | Yes | No | Limited | Yes | No |

Backend permission checks are required for every operation; hiding UI buttons is not authorization.
