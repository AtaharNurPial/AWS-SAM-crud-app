# from email import header
from email import message
import json
import os
#import uuid
import boto3


# import requests

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')

def lambda_handler(event, context):

    # if ('body' not in message or message['httpMethod'] != 'POST'):
    #     return{
    #     'statusCode': 400,
    #     'header': {},
    #     'body': json.dumps({
    #         'message': 'No Body!!!'})
    #     }

    
    # aws_environment = os.environ.get('AWSENV', 'AWS')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    activity = json.loads(event['body'])

    params = {
        #'id': str(uuid.uuid4()),
        'stage': activity['stage'], 
        'description': activity['description']
    }
    # response = table.put_item(
    #     TableName=table_name,
    #     Item=params
    # )
    # print(response)
   
    return {
        'statusCode': 200,
        'header': {},
        'body': json.dumps({
            'message': 'operation created'})
        }
