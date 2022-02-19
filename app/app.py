import json
import time
import boto3
from boto3.dynamodb.conditions import Key


def get_message(lang, dynamodb=None):

    client = boto3.client("dynamodb")

    response = client.get_item(TableName="Translations", Key=Key("lang").eq(lang))
    # time.sleep(1)
    return response["Items"]


def handler(event, context):
    if event["queryStringParameters"] == None:
        lang = "en"
    else:
        lang = event["queryStringParameters"]["lang"]

    try:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(get_message(lang)),
        }
    except Exception as e:
        print(e)
        return {"statusCode": 500}


if __name__ == "__main__":
    lang = "en"
    message = get_message(lang)
    print(message)
