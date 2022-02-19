import json
import time
import boto3
from boto3.dynamodb.conditions import Key

def get_message(lang, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    table = dynamodb.Table('Translations')
    response = table.query(
        KeyConditionExpression=Key('lang').eq(lang)
    )
    #time.sleep(1)
    return response['Items']

def handler(event, context):
    if not exists event['queryStringParameters']['lang']:
        lang = 'en'
    else:
        lang = event['queryStringParameters']['lang']

    try:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps(get_message(lang)),
        }
    except:
        return {
            'statusCode': 500
        }

if __name__ == '__main__':
    lang = 'en'
    message = get_message(lang)
    print(message)
