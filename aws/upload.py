import boto3
import os
from logger import logging

def upload_to_s3(local_file_path,bucket_name,s3_file_anme):
    s3 = boto3.client("s3",aws_access_key_id = os.getenv("access_id"),
                      aws_secret_access_key = os.getenv("secret_key"),
                      region_name = "us-east-1")
    
    try:
        s3.upload_file(local_file_path,bucket_name,s3_file_anme)
        logging.info("model was successfully uploaded to s3 bucket")
    except Exception as e:
        logging.error(f"error occured during uploading model into s3 bucket because {e}")
        raise

if __name__ == "__main__":
    upload_to_s3(local_file_path="model\inital_model.pth",bucket_name="animal-prediction",s3_file_anme="models/model.pth")