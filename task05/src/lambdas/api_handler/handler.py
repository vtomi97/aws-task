from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
#import boto3
#import uuid
#import json
#from datetime import datetime


_LOG = get_logger(__name__)


#dynamodb = boto3.resource('dynamodb', region_name="eu-central-1")
#table = dynamodb.Table("Events")


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        return event
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
