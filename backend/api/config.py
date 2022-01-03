"""Config."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""

    file_storage: str  # S3, Local
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_default_region = 'ap-northeast-1'
    bucket_name = 'hacarus-underground-staging-data'
