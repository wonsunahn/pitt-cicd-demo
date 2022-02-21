import boto3


def create_translation_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName="Translations",
        KeySchema=[{"AttributeName": "lang", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "lang", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    return table


if __name__ == "__main__":
    translation_table = create_translation_table()
    print("Table status:", translation_table.table_status)
