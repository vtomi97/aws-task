from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        const path = event["path"]
        method = event["httpMethod"]
        if path == "/hello" and method == "GET":
            return{
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            return{
                "statusCode": 400,
                "message": "Bad request syntax or unsupported method. Request path:" + path + ". HTTP method: " + method
            }
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
