import boto3
import sys
import json

s3 = boto3.client('s3')

def split_text(bucket, key, chunks=3):
    # Read file from S3
    obj = s3.get_object(Bucket=bucket, Key=key)
    text = obj['Body'].read().decode('utf-8')
    
    # Split text into words
    words = text.split()
    chunk_size = len(words) // chunks
    
    chunk_urls = []
    
    for i in range(chunks):
        start = i * chunk_size
        end = None if i == chunks-1 else (i+1)*chunk_size
        chunk_text = ' '.join(words[start:end])
        chunk_key = f'chunks/chunk_{i}.txt'
        s3.put_object(Bucket=bucket, Key=chunk_key, Body=chunk_text)
        chunk_urls.append(f's3://{bucket}/{chunk_key}')
    
    return chunk_urls

if __name__ == "__main__":
    bucket = sys.argv[1]      # e.g., 'my-wordcount-bucket'
    key = sys.argv[2]         # e.g., 'input/mytext.txt'
    urls = split_text(bucket, key)
    print(json.dumps(urls))   # Print chunk URLs
