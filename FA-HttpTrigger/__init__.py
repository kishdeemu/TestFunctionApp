import logging

import azure.functions as func
from . import sumNumbers

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    val1 = int(req.params.get('val1'))
    val2 = int(req.params.get('val2'))
    print("hey you are in live streaming logs", val1, val2)
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Sum of {val1} + {val2} = {sumNumbers.sum_numbers(val1, val2)}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
