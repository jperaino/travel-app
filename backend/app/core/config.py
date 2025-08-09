from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    environment: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()