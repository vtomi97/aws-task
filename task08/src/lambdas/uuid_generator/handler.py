from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import os
from datetime import datetime
import uuid
import json

_LOG = get_logger(__name__)


class UuidGenerator(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        id_array = []
        for i in range(10):
            id_array.append(str(uuid.uuid4()))
        json_data = {"ids": id_array}
        current_datetime = datetime.now()
        s3_client = boto3.client('s3')
        bucket_name = os.environ.get('target_bucket')
        file_name = current_datetime.isoformat()
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=(bytes(json.dumps(json_data).encode('UTF-8'))),
        )
        return 200
    

HANDLER = UuidGenerator()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
