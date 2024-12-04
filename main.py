import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

def list_first_blob():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the connection string and container name from environment variables
    source_connection_string = os.getenv("SOURCE_CONNECTION_STRING")
    source_container_name = os.getenv("SOURCE_CONTAINER_NAME")

    # Initialize the BlobServiceClient and ContainerClient
    source_blob_service_client = BlobServiceClient.from_connection_string(source_connection_string)
    source_container_client = source_blob_service_client.get_container_client(source_container_name)

    # List blobs and print the name of the first blob
    try:
        print("Listing the first blob in the source container:")
        blob_list = source_container_client.list_blobs()
        
        # Get the first blob
        first_blob = next(blob_list, None)
        if first_blob:
            print(f"First blob: {first_blob.name}")
        else:
            print("No blobs found in the container.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
list_first_blob()
