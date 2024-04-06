## The Purpose of this code is to incrementally post comments from the comments json file to kafka

# import necessary libraries
from kafka import KafkaProducer
import time
import random
import uuid

# Kafka server address
__bootstrap_server = "ed-kafka:29092"

def post_to_kafka(data):
    # Initialize Kafka producer with the bootstrap server address
    producer = KafkaProducer(bootstrap_servers=__bootstrap_server)
    
    # Generate a unique key for each message using UUID
    key = str(uuid.uuid4()).encode('utf-16')
    
    # Convert data to bytes (UTF-16 encoding)
    value = data.encode('utf-16')
    
    # Send data to a Kafka topic named 'comments-data' with a specified key
    producer.send('comments-data', key=key, value=value)
    
    # Ensure all buffered messages are sent to Kafka before closing the producer
    producer.flush()
    
    # Close the producer connection
    producer.close()
    
    # Print a message indicating that the data has been successfully posted to Kafka
    print("Posted to Kafka")


if __name__ == "__main__":
    # Path to the JSON file
    json_file = "/home/jovyan/kafka_spark_streaming/utils/comments(1).json"

    while True:
        # Open the JSON file in read mode with UTF-8 encoding
        with open(json_file, 'r', encoding='utf-8') as f:
            # Read the contents of the file
            data = f.read()

        # Post data read from the JSON file to Kafka
        post_to_kafka(data)
        
        # Print the data read from the JSON file
        print(data)

        # Sleep for 5 seconds before reading the file again
        time.sleep(5)
