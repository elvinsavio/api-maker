from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    
    db_host: str
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(env_file=".env")