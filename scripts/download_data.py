import boto3

s3 = boto3.resource("s3")

s3.meta.client.download_file(Bucket="10ac-batch-6", Key="data/w11/Challenge_Data.zip", Filename="./Challenge_Data.zip")