from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import boto3
import uuid
from datetime import datetime


_LOG = get_logger(__name__)


dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
table = dynamodb.Table("Events")


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        id = str(uuid.uuid4())
        current_datetime = datetime.now()
        iso_format = current_datetime.isoformat()

        if 'body' in event:
            data = json.loads(event['body'])
        else:
            data = {}
        item = {
            "id": id,
            "principalId": data["principalId"],
            "createdAt": iso_format,
            "body": data["content"]
        }
        
        table.put_item(Item=item)
                
        return {
            "statusCode": 201,
            "event": item
        }
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
