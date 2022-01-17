import json
import os
import boto3
from boto3.dynamodb.conditions import Key

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    # if not dynamodb:
    #     dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # else:
    #     dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table(table_name)
    activity = json.loads(event['body'])

    # response = table.get_item(
    #     Key={'id': activity}
    #     )
    # items = response['Item']
    # print(items)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'ItemID': '1234569'})
    }
