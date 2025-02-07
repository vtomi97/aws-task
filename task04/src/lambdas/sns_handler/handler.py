from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger(__name__)


class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        for record in event["Records"]:
            sns_message = record['Sns']['Message']
            print(sns_message)
        return 200
    

HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
