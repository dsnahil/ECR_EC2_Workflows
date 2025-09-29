import boto3
import sys
import json
import re

s3 = boto3.client('s3')

def count_words(bucket, key):
    # Read chunk from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read().decode('utf-8')
    
    # Normalize text: lowercase, remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    
    # Count occurrences
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    # Save counts as JSON to S3
    output_key = f'mapper-output/{key.split("/")[-1].replace(".txt",".json")}'
    s3.put_object(Bucket=bucket, Key=output_key, Body=json.dumps(counts))
    
    return f's3://{bucket}/{output_key}'

if __name__ == "__main__":
    bucket = sys.argv[1]  # e.g., 'my-wordcount-bucket-654654368158'
    key = sys.argv[2]     # e.g., 'chunks/chunk_0.txt'
    
    output_url = count_words(bucket, key)
    print(output_url)
