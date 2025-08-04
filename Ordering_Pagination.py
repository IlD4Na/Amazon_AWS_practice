import boto3 
import os
import logging 
from botocore.exceptions import ClientError

region_name = 'eu-west-3'

# Nome del bucket S3
bucket_name = 'test-aws-bucket-profession-ai-adi'

s3_client = boto3.client('s3', region_name=region_name) 

continuation_token = None 

# In run e Debug response è un dizionario che contiene diverse chiavi tra cui

'''
'responseMetadata': {altre chiavi e valori},
'IsTruncated': True/False,
'Contents': [{chiave1},{chiave2},{chiave3},...]
ecc..
'''
# Se IsTruncated ritorna True significa che ci sono altri file da elencare

ordered_list = []

while True:
    if continuation_token:
        response = s3_client.list_objects_v2(Bucket=bucket_name,MaxKeys=2,ContinuationToken=continuation_token)
    else:
        response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=2) 

    for item in response.get('Contents', []):
        ordered_list.append((item['Key'],item['LastModified']))
    
    if response.get('IsTruncated') is True:
        continuation_token = response.get('NextContinuationToken')
    else:

        ordered_list.sort(key=lambda x: x[1], reverse=True)  # Ordina per LastModified in ordine decrescente
        break

for key, last_modified in ordered_list:
            print(f"Key: {key}, LastModified: {last_modified}")
            print('\n')

print('\n \n Finito il ciclo while \n \n') 

