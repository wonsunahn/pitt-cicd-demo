from decimal import Decimal
import json
import boto3


def load_translations(translations, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Translations')
    for translation in translations:
        lang = translation['lang']
        message = translation['message']
        print("Adding translation:", lang, message)
        table.put_item(Item=translation)


if __name__ == '__main__':
    with open("data/translations.json") as json_file:
        translation_list = json.load(json_file, parse_float=Decimal)
    load_translations(translation_list)