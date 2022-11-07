import boto3 #Boto 3 is 
from botocore.exceptions import ClientError
import sys

# Create a bucket
def createBucket(bucket,region="eu-west-1"):
    try:
        s3 = boto3.client('s3', region_name=region) # Create a client connection
        location = {'LocationConstraint': region} # Set the region
        s3.create_bucket(Bucket=bucket,CreateBucketConfiguration=location) # Create the bucket
        print("Created bucket: " + bucket)
    except ClientError as e:
        print("\n" + e) # If there is an error, print the error
        return False
    return True

# Delete a bucket
def deleteBucket(bucket,region="eu-west-1"):
    try:
        s3 = boto3.client('s3', region_name=region)
        s3.delete_bucket(Bucket=bucket) # Delete the bucket
        print("Deleted bucket: " + bucket)
    except ClientError as e:
        print("\n" + e)
        return False
    return True

# Upload a file
def uploadFile(bucket,key,region="eu-west-1"): # Key is the file name
    try:
        s3 = boto3.client('s3', region_name=region)
        s3.upload_file(key, bucket, key) # Upload the file
        print("Uploaded file: " + key + " to bucket: " + bucket)
    except ClientError as e:
        print("\n" + e)
        return False
    return True

# Delete a file
def deleteFile(bucket,key,region="eu-west-1"):
    try:
        s3 = boto3.client('s3', region_name=region)
        s3.delete_object(Bucket=bucket, Key=key) # Delete the file
        print("Deleted file: " + key + " from bucket: " + bucket)
    except ClientError as e:
        print("\n" + e)
        return False
    return True

# List all buckets
def listFiles(bucket,region="eu-west-1"):
    try:
        s3 = boto3.client('s3', region_name=region)
        response = s3.list_objects_v2(Bucket=bucket) # List all files in the bucket
        for content in response['Contents']: # Loop through the files
            print(content['Key']) # Print the file names
    except ClientError as e:
        print("\n" + e)
        return False
    return True

# Download a file
def downloadFile(bucket,key,region="eu-west-1"):
    try:
        s3 = boto3.client('s3', region_name=region)
        s3.download_file(bucket, key, key)
        print("Downloaded file: " + key + " from bucket: " + bucket)
    except ClientError as e:
        print("\n" + e)
        return False
    return True

# If this script is run directly, call the function specified in the first argument
if __name__ == "__main__":
    globals()[sys.argv[1]](*sys.argv[2:])