import boto3
import pytest
import json

from moto import mock_dynamodb2
from app.app import lambda_handler, get_message


DYNAMODBRESPONSE = {
    "Item": {"lang": {"S": "en"}, "message": {"S": "Hello World"}},
    "ResponseMetadata": {
        "RequestId": "c4c5229b-ae73-46cc-89b1-c5f46874717b",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Sat, 19 Feb 2022 16:40:52 GMT",
            "content-type": "application/x-amz-json-1.0",
            "x-amz-crc32": "2656284382",
            "x-amzn-requestid": "c4c5229b-ae73-46cc-89b1-c5f46874717b",
            "content-length": "58",
            "server": "Jetty(9.4.18.v20190429)",
        },
        "RetryAttempts": 0,
    },
}
EVENTRESPONSE = {
    "resource": "/",
    "path": "/",
    "httpMethod": "GET",
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "s_fid=7AAB6XMPLAFD9BBF-0643XMPL09956DE2; regStatus=pre-register",
        "Host": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-5e66d96f-7491f09xmpl79d18acf3d050",
        "X-Forwarded-For": "52.255.255.12",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
    },
    "multiValueHeaders": {
        "accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        ],
        "accept-encoding": ["gzip, deflate, br"],
        "accept-language": ["en-US,en;q=0.9"],
        "cookie": ["s_fid=7AABXMPL1AFD9BBF-0643XMPL09956DE2; regStatus=pre-register;"],
        "Host": ["70ixmpl4fl.execute-api.ca-central-1.amazonaws.com"],
        "sec-fetch-dest": ["document"],
        "sec-fetch-mode": ["navigate"],
        "sec-fetch-site": ["none"],
        "upgrade-insecure-requests": ["1"],
        "User-Agent": [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        ],
        "X-Amzn-Trace-Id": ["Root=1-5e66d96f-7491f09xmpl79d18acf3d050"],
        "X-Forwarded-For": ["52.255.255.12"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "2gxmpl",
        "resourcePath": "/",
        "httpMethod": "GET",
        "extendedRequestId": "JJbxmplHYosFVYQ=",
        "requestTime": "10/Mar/2020:00:03:59 +0000",
        "path": "/Prod/",
        "accountId": "123456789012",
        "protocol": "HTTP/1.1",
        "stage": "Prod",
        "domainPrefix": "70ixmpl4fl",
        "requestTimeEpoch": 1583798639428,
        "requestId": "77375676-xmpl-4b79-853a-f982474efe18",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "52.255.255.12",
            "principalOrgId": None,
            "accessKey": None,
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "user": None,
        },
        "domainName": "70ixmpl4fl.execute-api.us-east-2.amazonaws.com",
        "apiId": "70ixmpl4fl",
    },
    "body": None,
    "isBase64Encoded": False,
}

TXNS_TABLE = "Translations"


@pytest.fixture
def use_moto():
    @mock_dynamodb2
    def dynamodb_client():
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")

        # Create the table
        dynamodb.create_table(
            TableName=TXNS_TABLE,
            KeySchema=[{"AttributeName": "lang", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "lang", "AttributeType": "S"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        return dynamodb

    return dynamodb_client


@mock_dynamodb2
def test_handler_for_failure(use_moto):
    use_moto()
    event = EVENTRESPONSE

    return_data = lambda_handler(event, "")
    assert return_data["statusCode"] == 500
    assert return_data["error"] == "No Records Found."


@mock_dynamodb2
def test_handler_for_status_ok(use_moto):
    use_moto()
    table = boto3.resource("dynamodb", region_name="us-east-1").Table(TXNS_TABLE)
    table.put_item(Item={"lang": "en", "message": "Hello World"})

    event = EVENTRESPONSE

    return_data = lambda_handler(event, "")
    print(json.dumps(return_data, indent=2))
    body = json.loads(return_data["body"])

    assert return_data["statusCode"] == 200
    assert body["Lang"] == "en"
    assert body["Message"] == "Hello World"
