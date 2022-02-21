import os
import json
import time
import boto3

TABLE_NAME = os.environ["TableName"]
# Get the environment, so we can run appropriate scripts
IS_DEVELOPMENT = os.environ["STAGE"] == "DEVELOPMENT"


def get_dynamo_db_client():
    """Set the dynamodb instance based on environment"""
    if IS_DEVELOPMENT:
        # Set the boto3 session for dynamodb if its development environment
        dynamo_db_session = boto3.Session(profile_name="default")
        return dynamo_db_session.resource("dynamodb")
    else:
        return boto3.resource("dynamodb")


DYNAMO_DB = get_dynamo_db_client()


def get_message(lang):
    """
    This function will check the entry in dynamodb if exists will return item
    :param lang
    :return: message or return NoRecordError Exception
    """

    table = DYNAMO_DB.Table(TABLE_NAME)

    response = table.get_item(
        Key={"lang": {"S": lang}},
        ProjectionExpression="lang, message",
        ConsistentRead=True,
    )

    # time.sleep(1)

    if "Item" not in response:
        raise NoRecordError("No Record Found.")
    else:
        return response["Item"]


def lambda_handler(event, context):
    if event["queryStringParameters"] == None:
        lang = "en"
    else:
        lang = event["queryStringParameters"]["lang"]

    try:
        if event["queryStringParameters"] == None:
            lang = "en"
        else:
            lang = event["queryStringParameters"]["lang"]

        result = get_message(lang)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps(result, default=lambda o: o.__dict__),
        }
    except Exception as e:
        return {"statusCode": 500, "error": str(e)}


class Error(Exception):
    """Base class for other exceptions"""

    pass


class NoRecordError(Error):
    """Raised when no record found"""

    pass


if __name__ == "__main__":
    lang = "en"
    message = get_message(lang)
    print(message)
