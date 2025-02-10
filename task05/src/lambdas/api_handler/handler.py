from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import uuid
import json
from datetime import datetime


_LOG = get_logger(__name__)


dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
table = dynamodb.Table("Events")


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        id = uuid.uuid4()
        current_datetime = datetime.now()
        iso_format = current_datetime.isoformat()

        item = {
            "id": id,
            "principalId": 101,
            "createdAt": iso_format,
            "body": "test_body"
        }
        
        table.put_item(Item=item)
                
        return {"statusCode": 201}
        
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
