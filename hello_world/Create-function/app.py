import json
import os
#import uuid
import boto3

# import requests

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/618758721119/sam-crud-RawQueue-5H7I5MQWO96P'

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
    activity = json.loads(event["body"])
    sqs = boto3.client('sqs')

    sqs_response = sqs.send_message(
    QueueUrl = queue_url,
    MessageBody = json.dumps(event["body"])
    )
    print(sqs_response.get('messageId'))

    params = {
        'stage': activity['stage'], 
        'description': activity['description']
    }
    table_response = table.put_item(
        TableName=table_name,
        Item=params
    )
    print(table_response)
   
    return {
        'statusCode': 200,
        'header': {},
        'body': json.dumps({'message': 'Activity Created!!!'})
    }
