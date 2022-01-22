import json
import os
import boto3

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/618758721119/sqs-practice-RawQueue-9TQ7R07SNNU6'

def lambda_handler(message, context):

    dynamodb = boto3.resource('dynamodb')
    # if not dynamodb:
    #     dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # else:
    #     dynamodb = boto3.resource('dynamodb',  region_name=region)
        
    table = dynamodb.Table(table_name)
    activity = json.loads(message['body'])
    sqs = boto3.client('sqs')

    sqs_response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
         },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)


    params = {
        'id': activity['id']
        # 'description': activity['description']
    }

    table_response = table.update_item(
        Key = params,
        UpdateExpression = "set stage = :s, description = :d",
        ExpressionAttributeValues = {
            ':s': activity['stage'],
            ':d': activity['description']
        },
        ReturnValues = "UPDATED_NEW"
    )
    print(table_response)

    return{
        'statusCode': 200,
        'headers': {},
        'messageId': json.dumps(sqs_response['MessageId']),
        'body': json.dumps({'message': 'Operation updated'})
    }
