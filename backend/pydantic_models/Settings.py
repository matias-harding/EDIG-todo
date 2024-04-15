from fastapi import FastAPI
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    user: str
    password: str
    database: str
    host: str
    port: str

    class Config:
        env_file = ".env"

settings = Settings()

