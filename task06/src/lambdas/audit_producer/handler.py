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
                        
        for record in event["Records"]:
            event_name = record["eventName"]
            
            if event_name == "INSERT":
                new_image = record["dynamodb"]["NewImage"]
                item = {
                    "id": id,
                    "itemKey": new_image["key"]["S"],
                    "modificationTime": iso_format,
                    "newValue": {
                        "key": new_image["key"]["S"],
                        "value": int(new_image["value"]["N"])
                    }
                }
                table.put_item(Item=item)
            elif event_name == "MODIFY":
                new_image = record["dynamodb"]["NewImage"]
                old_image = record["dynamodb"]["OldImage"]
                if new_image["key"]["S"] != old_image["key"]["S"]:
                    item = {
                        "id": id,
                        "itemKey": new_image["key"]["S"],
                        "modificationTime": iso_format,
                        "updatedAttribute": "key",
                        "oldValue": old_image["key"]["S"],
                        "newValue": new_image["key"]["S"]
                    }
                    table.put_item(Item=item)
                elif new_image["value"]["N"] != old_image["value"]["N"]:
                    item = {
                        "id": id,
                        "itemKey": new_image["key"]["S"],
                        "modificationTime": iso_format,
                        "updatedAttribute": "value",
                        "oldValue": int(old_image["value"]["N"]),
                        "newValue": int(new_image["value"]["N"])
                    }
                    table.put_item(Item=item)
            else:
                print(event_name)
                        
        return 200
    

HANDLER = AuditProducer()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)