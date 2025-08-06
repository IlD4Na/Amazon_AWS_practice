import boto3 
import csv 

def send_data_firehose(name_file_csv, name_stream_firehose):
    """Send data froma CSV file to Amazon Kinesis Firehose delivery stream. 
    
    parameters:
    name_file_csv (str): The name of the CSV file to read data from.
    name_stream_firehose (str): The name of the Kinesis Firehose delivery stream to send data to.
    """
    # Creation of a client to interact with Kinesis Firehose
    client = boto3.client('firehose', region_name='eu-west-3')

    # Open the CSV file and read its content in read modality with r 
    with open(name_file_csv, 'r') as file_csv:
        reader_csv = csv.reader_csv(file_csv)
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
            print(f"Record sent with ID: {response['RecordId']}")

# Using the function 
name_file_csv = 'data.csv'
name_stream_firehose = 'my-firehose-stream'
send_data_firehose(name_file_csv, name_stream_firehose)