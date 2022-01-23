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
    print(sqs_response.get('MessageId'))

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
