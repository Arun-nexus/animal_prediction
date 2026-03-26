import boto3

s3 = boto3.client("s3")

bucket = "youtube_extension"
key = "models/animal_model/model_v1.pth"

s3.download_file(bucket, key, "model/initial_model.pth")