# Security requirements before production

Do not expose this starter publicly: it has no authentication or persistent authorization. Before production, implement modern password hashing, secure HTTP-only/SameSite cookies, CSRF, MFA for privileged users, rate limiting, server-side object authorization, audit logs, secret rotation, mTLS/short-lived node credentials, signed idempotent jobs, strict upload validation, quotas, encrypted backups and tested restore. Never accept browser-supplied shell commands, expose Docker/libvirt sockets, store raw card details, or trust payment screenshots.
