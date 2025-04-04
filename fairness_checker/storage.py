import boto3
import pandas as pd
import json
import os

class S3Storage:
    def __init__(self, config):
        self.bucket = config.S3_BUCKET
        self.prefix = config.S3_PREFIX
        self.output_prefix = config.OUTPUT_PREFIX
        self.s3 = boto3.client('s3', region_name=config.AWS_REGION)

    def list_csv_files(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=self.prefix)
        return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.csv')]

    def read_csv(self, key):
        response = self.s3.get_object(Bucket=self.bucket, Key=key)
        return pd.read_csv(response['Body'])

    def write_report(self, report, original_key):
        base_name = os.path.basename(original_key).replace('.csv', '_fairness.json')
        output_key = f"{self.output_prefix}{base_name}"
        self.s3.put_object(Bucket=self.bucket, Key=output_key, Body=json.dumps(report).encode('utf-8'))
        print(f"[INFO] Report saved to s3://{self.bucket}/{output_key}")

