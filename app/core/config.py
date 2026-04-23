from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ArchReactor"
    DEBUG: bool = False
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/archreactor"
    SECRET_KEY: str = "change-me-in-production"

    JWT_SECRET_KEY: str = "change-me-jwt-secret"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
