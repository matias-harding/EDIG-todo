from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = "EDIG_TODO"
    user: str = "todo"
    password: str = "todo"
    host: str = "localhost"
    port: int = 5432

