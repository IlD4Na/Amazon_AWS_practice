import boto3 

import os

import logging 

from botocore.exceptions import ClientError

region_name = 'eu-west-3'

# Nome del bucket S3
bucket_name = 'test-aws-bucket-profession-ai-adi'


file_name = 'ESAME DATA ANALYST I ED Adrian Marius Ginghina.pdf'

path_sub_folder = 'a/b/c/d'

Saved_file_path = os.path.join(path_sub_folder, file_name)

print(f"Saved_file_path: {Saved_file_path}")


# Upload the file 
def upload_file_to_s3(file_name, bucket_name, Saved_file_path, region_name=region_name):
    """Upload a file to an S3 bucket. """


    s3_client = boto3.client('s3', region_name=region_name)
    try:
        response = s3_client.upload_file(file_name, bucket_name, Saved_file_path)
        print(f"File {file_name} uploaded successfully to {bucket_name}/{Saved_file_path}.")
    except ClientError as e:
        logging.error(e)
    print(f"File {Saved_file_path} uploaded successfully in the bucket {bucket_name}.")


upload_file_to_s3(file_name, bucket_name, Saved_file_path, region_name=region_name)


print('\n Programma finito con successo! \n')



