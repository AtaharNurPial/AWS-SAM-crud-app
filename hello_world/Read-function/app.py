import json
import os
import boto3
from boto3.dynamodb.conditions import Key

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')

def lambda_handler(message, context):

    dynamodb = boto3.resource('dynamodb')
    # if not dynamodb:
    #     dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # else:
    #     dynamodb = boto3.resource('dynamodb',  region_name=region)
        
    table = dynamodb.Table(table_name)
    activity_id = message['pathParameters']['id']

    response = table.query(
        KeyConditionExpression=Key('id').eq(activity_id)
    )
    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }
