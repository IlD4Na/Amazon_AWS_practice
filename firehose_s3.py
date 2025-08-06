import boto3 
import csv 
import time 
from datetime import datetime
import random

def send_data_firehose(name_file_csv, name_stream_firehose):
    """Send data froma CSV file to Amazon Kinesis Firehose delivery stream. 
    
    parameters:
    name_file_csv (str): The name of the CSV file to read data from.
    name_stream_firehose (str): The name of the Kinesis Firehose delivery stream to send data to.
    """
    # Creation of a client to interact with Kinesis Firehose
    client = boto3.client('firehose', region_name='us-east-1') #check the region

    # Open the CSV file and read its content in read modality with r 
    with open(name_file_csv, 'r') as file_csv:
        reader_csv = csv.reader(file_csv)
        next(reader_csv)  # Skip the header row if present

        # Iterate through each row in the CSV file
        for row in reader_csv:
            #Convert the row ina string format, assuming all fields are separated by commas
            data = ','.join(row) + '\n'

            # Send the data to the Kinesis Firehose delivery stream
            response = client.put_record(
                DeliveryStreamName=name_stream_firehose,
                Record={'Data': data.encode('utf-8')}
            )

            # Print the ID of the record sent
            print(f"Record sent with ID: {response['RecordId']}\n")


def append_new_row_to_csv(file_path):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [now, f"sensor_{random.randint(1,5)}", random.uniform(10, 100)]
        writer.writerow(row)

# Using the function 
name_file_csv = 'data/firehose_test.csv'
name_stream_firehose = 'demo_s3' # The name I chosed in the AWS Console


'''
Inizialmente non andava perche avevo sbagliato la regione e avevo messo mare il percorso
relativo del file in csv
'''

#Proviamo a farlo andare in continuo per 3/4 volte

for contatore in range(5):
    append_new_row_to_csv(name_file_csv)
    send_data_firehose(name_file_csv, name_stream_firehose)
    print("Data sent to Firehose delivery stream.")
    print("\n")
    time.sleep(5)  
# Wait for 5 seconds before sending the next record

print("All data sent successfully to Firehose delivery stream.")
print("\nProgram finished successfully!\n")


    