from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json

_LOG = get_logger(__name__)


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        response = {
            "statusCode": 201,
            "body": json.dumps({
                "message": "TEST"
            }),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
    

HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
