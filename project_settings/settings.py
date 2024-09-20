import os

from pydantic.v1 import BaseSettings
from pydantic import computed_field

from functools import cached_property


class Settings(BaseSettings):
    PROJECT_NAME: str = "City temperature management"

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: int = os.getenv("DB_PORT")

    class Config:
        case_sensitive = True
        env_file = ".env"

    @computed_field
    @cached_property
    def DATABASE_URL(self) -> str:
        return str(
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}",
            f"@db:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
