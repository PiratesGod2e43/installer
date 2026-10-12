#!/usr/bin/env bash
set -Eeuo pipefail
umask 077
fail(){ printf 'ERROR: %s\\n' "$*" >&2; exit 1; }
[[ $EUID -eq 0 ]] || fail "Run with sudo/root; this preflight makes no system changes."
[[ -f .env ]] || fail "Missing .env. Copy .env.example to .env and configure it."
domain="$(awk -F= '$1=="PANEL_DOMAIN" {sub(/^[^=]*=/,""); print; exit}' .env)"
[[ "$domain" =~ ^[A-Za-z0-9.-]+$ ]] || fail "PANEL_DOMAIN must be a hostname without scheme/path."
grep -q 'CHANGE_ME' .env && fail "Replace placeholder values in .env."
printf '%s\\n' "Basic preflight passed." "No packages, users, services, firewall, DNS, TLS, databases or Pterodactyl resources were changed." "Production deployment is not implemented."
