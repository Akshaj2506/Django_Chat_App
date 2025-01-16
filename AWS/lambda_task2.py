import boto3
import base64
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_name = event.get('file_name')
        file_content = event.get('file_content')  # Base64-encoded content
        bucket_name = event.get('bucket_name')

        if not file_name or not file_content or not bucket_name:
            return {
                'statusCode': 400,
                'body': 'Missing required parameters: file_name, file_content, or bucket_name'
            }

        decoded_file_content = base64.b64decode(file_content)

        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=decoded_file_content
        )

        return {
            'statusCode': 200,
            'body': f'Successfully uploaded {file_name} to {bucket_name}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
