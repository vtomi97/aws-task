from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json
import boto3 
import os
import uuid
from datetime import datetime


_LOG = get_logger(__name__)


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
    
        dynamodb = boto3.resource('dynamodb') 
        table = dynamodb.Table(os.environ.get('target_table'))
        
        id = str(uuid.uuid4())
        
        current_datetime = datetime.now()
        iso_format = current_datetime.isoformat()
                
        new_item = {
            "id": id,
            "principalId": event["principalId"],
            "body": event["content"],
            "createdAt": iso_format,
        }
        
        table.put_item(Item=new_item)
        
        response = {
            "statusCode": 201,
            "body": json.dumps({
                "event": new_item
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)