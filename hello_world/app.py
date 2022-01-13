# from email import header
import json
import os
#import uuid
import boto3


# import requests


def lambda_handler(event, context):

    table_name = os.environ.get('TABLE', 'Activities')
    # region = os.environ.get('REGION', 'us-east-2')
    # aws_environment = os.environ.get('AWSENV', 'AWS')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    activity = json.loads(event['body'])

    params = {
        #'id': str(uuid.uuid4()),
        'stage': activity['stage'],
        'description': activity['description']
    }
    response = table.put_item(
        TableName=table_name,
        Item=params
    )
    print(response)
   
    return {
        "statusCode": 200,
        'header': {},
        "body": json.dumps({
            "message": "operation created",
        }),
    }
