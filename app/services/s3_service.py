from botocore.exceptions import ClientError
from app.infrastructure.s3_client import get_s3_client
from app.config import Config

class S3Service:
    def __init__(self):
        self.s3_client = get_s3_client()
        self.bucket_name = Config.BUCKET_NAME

    def ensure_bucket_exists(self):
        try:
            self.s3_client.create_bucket(Bucket=self.bucket_name)
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code')
            if error_code not in ['BucketAlreadyOwnedByYou', 'BucketAlreadyExists']:
                raise e

    def list_files(self):
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        return [obj['Key'] for obj in response.get('Contents', [])]

    def upload_file(self, file_obj, filename):
        self.s3_client.upload_fileobj(file_obj, self.bucket_name, filename)

    def download_file(self, file_id):
        try:
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_id)
            return obj['Body'].read()
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                return None
            raise e

    def delete_file(self, file_id):
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=file_id)
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_id)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                return False
            raise e
