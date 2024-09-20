import os
from dotenv import load_dotenv

from pydantic.v1 import BaseSettings
from pydantic import computed_field

from functools import cached_property


load_dotenv(".env")


class Settings(BaseSettings):
    PROJECT_NAME: str = "City temperature management"

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: int = os.getenv("DB_PORT")

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

DATABASE_URL = "".join([
    f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}",
    f"@db:{settings.DB_PORT}/{settings.DB_NAME}"
])
