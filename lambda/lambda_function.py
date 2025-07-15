import json
import os
from datetime import datetime
import boto3

s3 = boto3.client('s3')
bucket = os.environ.get('BUCKET_NAME')

def lambda_handler(event, context):
    key = f"file_{datetime.utcnow().isoformat()}.txt"
    s3.put_object(Bucket=bucket, Key=key, Body="created by lambda")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "File created", "key": key})
    }
