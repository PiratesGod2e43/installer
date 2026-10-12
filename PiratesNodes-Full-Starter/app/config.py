from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "PiratesNodes"
    app_env: str = "development"
    panel_domain: str = "panel.example.com"
    app_secret: str = "CHANGE_ME_TO_A_RANDOM_SECRET_AT_LEAST_32_CHARACTERS"
    minecraft_provisioning_enabled: bool = False
    vps_provisioning_enabled: bool = False
    payments_enabled: bool = False
    discord_integration_enabled: bool = False
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

settings = Settings()
