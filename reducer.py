import boto3
import sys
import json

s3 = boto3.client('s3')

def reduce_counts(bucket, keys):
    final_counts = {}
    
    for key in keys:
        # Download mapper output
        obj = s3.get_object(Bucket=bucket, Key=key)
        mapper_counts = json.loads(obj['Body'].read().decode('utf-8'))
        
        # Aggregate counts
        for word, count in mapper_counts.items():
            final_counts[word] = final_counts.get(word, 0) + count
    
    # Save final counts to S3
    output_key = 'final-word-counts.json'
    s3.put_object(Bucket=bucket, Key=output_key, Body=json.dumps(final_counts))
    
    return f's3://{bucket}/{output_key}'

if __name__ == "__main__":
    bucket = sys.argv[1]      # e.g., 'my-wordcount-bucket-654654368158'
    mapper_keys = sys.argv[2:]  # e.g., 'mapper-output/chunk_0.json' 'mapper-output/chunk_1.json' ...
    
    final_url = reduce_counts(bucket, mapper_keys)
    print(final_url)
