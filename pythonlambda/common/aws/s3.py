from . import resource_client

def upload_to_bucket(inputfile, bucket, objectfile):
    s3client = resource_client.get('s3')
    s3client.upload_file(inputfile, bucket,objectfile)