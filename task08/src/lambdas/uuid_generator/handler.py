from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import os
from datetime import datetime

_LOG = get_logger(__name__)


class UuidGenerator(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        current_datetime = datetime.now()
        s3_client = boto3.client('s3')
        bucket_name = os.environ.get('target_bucket')
        file_name = current_datetime.isoformat()
        file_content = "TESTFILE"
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )
        return 200
    

HANDLER = UuidGenerator()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
