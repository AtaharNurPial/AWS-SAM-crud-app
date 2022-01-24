import json
import os
import boto3

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')
queue_url = 'https://sqs.us-east-2.amazonaws.com/618758721119/sqs-practice-RawQueue-9TQ7R07SNNU6'

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    # activity_id = event['id']
    # activity_date = event['date']
    activity = json.loads(event['body'])
    sqs = boto3.client('sqs')

    sqs_response = sqs.send_message(
    QueueUrl = queue_url,
    MessageBody = json.dumps(event['body'])
    )
    print(sqs_response.get('messageId'))

    params = {
        'id': activity['id'],
        'date': activity['date']
    }

    table_response = table.delete_item(
        Key = params
    )
    print(table_response)

    return{
        'statusCode': 200,
        'headers': {},
        # 'messageId': json.dumps(sqs_response['MessageId']),
        'body': json.dumps({'message': 'Operation Deleted'})
    }
