import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!!!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def hello2(event, context):
    body = {
        "message": "Heeeeeellllooooo!!!!!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
