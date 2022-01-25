import json
import os
import boto3

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/618758721119/sam-crud-RawQueue-5H7I5MQWO96P'

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    # if not dynamodb:
    #     dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # else:
    #     dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table(table_name)
    activity = json.loads(event['body'])
    sqs = boto3.client('sqs')

    sqs_response = sqs.send_message(
    QueueUrl = queue_url,
    MessageBody = json.dumps(event['body'])
    )
    print(sqs_response.get('messageId'))

    table_response = table.get_item(
        Key={'id': activity}
        )
    print(table_response)

    return {
        'statusCode': 200,
        'headers': {},
        # 'messageId': json.dumps(sqs_response['MessageId']),
        'body': json.dumps({'message': 'message sent...'})
    }
