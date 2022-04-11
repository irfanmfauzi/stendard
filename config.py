from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DB_ENGINE: str
    DB_USERNAME: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"


@lru_cache
def get_setting():
    return Settings()


setting = get_setting()
