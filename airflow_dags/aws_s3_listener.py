import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class AWSS3Listener(BaseOperator):
    @apply_defaults
    def __init__(self, bucket_name, prefix, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bucket_name = bucket_name
        self.prefix = prefix

    def execute(self, context):
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=self.bucket_name, Prefix=self.prefix)
        for obj in response.get('Contents', []):
            self.log.info(f'Detected object: {obj['Key']}')