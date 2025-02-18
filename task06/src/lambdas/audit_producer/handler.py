from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json
import boto3 
import os
import uuid
from datetime import datetime


_LOG = get_logger(__name__)


class AuditProducer(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
    
        dynamodb = boto3.resource('dynamodb') 
        table = dynamodb.Table(os.environ.get('target_table'))
        
        id = str(uuid.uuid4())
        
        current_datetime = datetime.now()
        iso_format = current_datetime.isoformat()
        
        print(event)
        
        key = ""
        value = 0
        
        for record in event["Records"]:
            event_name = record["eventName"]
            
            if event_name == "INSERT":
                new_image = record["dynamodb"]["NewImage"]
                key = new_image["value"]["N"]
                value = new_image["key"]["S"]
            elif event_name == "MODIFY":
                print("MODIFY")
            else:
                print(event_name)
                
        print("KEY: " + key)
        print("VALUE: " + value)
        
        new_item = {
            "id": id,
            "itemKey": key,
            "modificationTime": iso_format,
            "newValue": {
                "key": key,
                "value": value
            }
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
        return 200
    

HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)