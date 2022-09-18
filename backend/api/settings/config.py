from functools import lru_cache
from typing import Literal, Optional

from pydantic import BaseSettings


class Config(BaseSettings):
    table_name: str
    table_host: str
    region: str
    aws_profile: str
    
    class Config:
        env_file = ".env.development"

@lru_cache
def get_settings() -> Config:
    return Config()