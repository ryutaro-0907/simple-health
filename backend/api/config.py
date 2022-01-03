"""Config."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""

    file_storage: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_default_region = ''
    bucket_name = ''
