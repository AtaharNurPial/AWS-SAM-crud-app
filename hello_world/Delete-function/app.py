import json
import os
import boto3

table_name = os.environ.get('TABLE', 'Activities')
region = os.environ.get('REGION', 'us-east-2')

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    # activity_id = event['id']
    # activity_date = event['date']
    activity = json.loads(event['body'])

    params = {
        'id': activity['id'],
        'date': activity['date']
    }

    # response = table.delete_item(
    #     Key = params
    # )
    # print(response)

    return{
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'message': 'Operation Deleted'})
    }
