import boto3 

# Nome del bucket S3
bucket_name = 'test-aws-bucket-profession-ai-adi'

# Creazione del client S3
s3_client = boto3.client('s3', region_name='eu-west-3')

def list_files(bucket):
    """Elenca tutti i file in un bucket S3."""
    try:
        contents =[]
        for items in s3_client.list_objects(Bucket=bucket)['Contents']:
            contents.append(items['Key'])
        return contents
    except Exception as e:
        print(f"Errore durante l'elenco dei file: {e}")
        return None
    
# Esempio di utilizzo della funzione per capire con il run debug cosa c'è dentro il bucket
bucket_content = s3_client.list_objects(Bucket=bucket_name)

print('boh') #Usato per poter eseguire il debug


if __name__ == "__main__":
    files = list_files(bucket_name)
    print(files)
