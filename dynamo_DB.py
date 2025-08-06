import time 
import boto3

# Assuming AWS credentials are configured in the environment or through AWS CLI
region_name = 'eu-west-3'

# We define a new service resource for DynamoDB
dynamodb = boto3.resource('dynamodb', region_name=region_name)


# We define the table we want to interact with, we can find it in AWS Glue
# or in the AWS Console under DynamoDB
table = dynamodb.Table('professionai')

#Items we want to upload to the table

items = [
    {
        "cod_fiscale": "A123",
        "nome": "Adrian Marius",
        "cognome": "Ginghina",
        "Age": 27,
        "occupation": "Data Engineer",
        "created_at": int(time.time()),
        "pets": [{"name":"Milo","type":"dog"},{"name":"Mia","type":"cat"}]
    },
    {"cod_fiscale": "B456","name":"Alberto","surname":"Rossi",
     "Age":30,"occupation":"Data Scientist","created_at":int(time.time())},
{        "cod_fiscale": "C789",
        "name": "Maria",
        "surname": "Bianchi",
        "Age": 25,
        "occupation": "Data Analyst",
        "created_at": int(time.time()),
        "hobbies":["Skydiving", "Photography"]}
]

for item in items:
    table.put_item(Item=item)

print("\nItems uploaded successfully to DynamoDB table 'professionai'.")

time.sleep(8)

# Readng an item by partition key
response = table.get_item(Key={"cod_fiscale": "A123"})

item = response.get('Item', {})

print(f"\nRetrieved item: {item}")

#Scanning the table to get all items (use with caution)
response = table.scan()
items = response.get('Items', [])
print(f"\nAll items in the table: {items}")


# We can pretty print with json and pprint