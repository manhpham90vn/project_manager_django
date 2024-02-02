from celery import shared_task
import boto3
from projectmanager.settings import LAMDA_ARN

@shared_task
def invoke_lambda():
    client = boto3.client('lambda')
    invoke = client.invoke(
        FunctionName=LAMDA_ARN,
        InvocationType='RequestResponse', # RequestResponse | Event
    ) 
    response = invoke['Payload'].read().decode('utf-8')
    return response