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
    activity = json.loads(message['body'])

    params = {
        'id': activity['id']
        # 'description': activity['description']
    }

    # response = table.update_item(
    #     Key = params,
    #     UpdateExpression = "set stage = :s, description = :d",
    #     ExpressionAttributeValues = {
    #         ':s': activity['stage'],
    #         ':d': activity['description']
    #     },
    #     ReturnValues = "UPDATED_NEW"
    # )
    # print(response)

    return{
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'message': 'Operation updated'})
    }
