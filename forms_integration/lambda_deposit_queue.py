import boto3
import json 
client = boto3.client('sqs')
QueueURL = 'https://sqs.us-east-1.amazonaws.com/566269010243/zhongwei_forms_queue'

def lambda_handler(event, context):
   
    dict_string = json.dumps(event)
    response = client.send_message(
        QueueUrl = QueueURL,
        MessageBody = dict_string,    
    )
    
    print("Queue Response "+json.dumps(response))
