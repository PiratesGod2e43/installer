from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0-scaffold",
    description="Independent PiratesNodes starter. Provisioning is disabled by default.",
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url=None,
)

class BrandingUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    primary_color: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$")
    support_url: str | None = Field(default=None, max_length=300)

@app.get("/health", tags=["operations"])
def health():
    return {"status": "ok", "app": settings.app_name, "environment": settings.app_env}

@app.get("/api/v1/status", tags=["platform"])
def platform_status():
    return {
        "name": settings.app_name,
        "version": "0.1.0-scaffold",
        "provisioning": {"minecraft": settings.minecraft_provisioning_enabled, "kvm_vps": settings.vps_provisioning_enabled},
        "payments_enabled": settings.payments_enabled,
        "discord_enabled": settings.discord_integration_enabled,
        "warning": "No authentication, persistence, billing engine, or node agent. Do not expose publicly.",
    }

@app.post("/api/v1/owner/branding", tags=["owner"], status_code=501)
def update_branding(payload: BrandingUpdate):
    raise HTTPException(status_code=501, detail="Placeholder until secure authentication, RBAC, audit logging and persistence exist.")

@app.post("/api/v1/provision/minecraft", tags=["provisioning"], status_code=503)
def provision_minecraft():
    if not settings.minecraft_provisioning_enabled:
        raise HTTPException(status_code=503, detail="Minecraft provisioning is disabled in this starter.")
    raise HTTPException(status_code=501, detail="Provisioning worker and secure node agent are not implemented.")

@app.post("/api/v1/provision/vps", tags=["provisioning"], status_code=503)
def provision_vps():
    if not settings.vps_provisioning_enabled:
        raise HTTPException(status_code=503, detail="KVM VPS provisioning is disabled in this starter.")
    raise HTTPException(status_code=501, detail="KVM provisioning worker and secure node agent are not implemented.")
