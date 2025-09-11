from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    APP_ENV: str = "dev"
    APP_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    SERVICE_NAME: str = "api-onprem"
    HTTP_HOST: str = "0.0.0.0"
    HTTP_PORT: int = 8000
    ENABLE_CORS: bool = True
    DATA_PATH: str = "/app/data"
    SLOW_DELAY: int = 5
    ADMIN_USER: str = "Admin"
    ADMIN_PASS: str = "root"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
