import azure.functions as func
import datetime
import json
import logging
from core import handler

app = func.FunctionApp()

@app.route(route="linebot-housedreamer", auth_level=func.AuthLevel.ANONYMOUS)
def linebot_housedreamer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Yahoo~ Yeah~")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="callback", auth_level=func.AuthLevel.ANONYMOUS)
def linebot_message_handler(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Start handling linebot messages...')
    # get X-Line-Signature header value
    signature = req.headers.get('x-line-signature')
    logging.info(f'headers={signature}') 
    # logging.info(f'handler={handler}') 

    # get request body as text
    body = req.get_body().decode('utf-8')
    # logging.info("Request body: " + body)

    try:
        handler.handle(body, signature)
        pass
    except ValueError:
        pass
    return func.HttpResponse('OK')

    # return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
    # return func.HttpResponse('OK')