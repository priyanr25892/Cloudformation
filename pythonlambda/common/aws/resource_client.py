import boto3

def get(resourcename):
    return boto3.client(resourcename)
