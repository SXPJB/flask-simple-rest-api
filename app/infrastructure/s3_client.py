import boto3
from app.config import Config

def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=Config.AWS_ENDPOINT_URL,
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region_name=Config.AWS_DEFAULT_REGION
    )
