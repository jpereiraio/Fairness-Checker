import os

class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    S3_BUCKET = os.getenv('S3_BUCKET')
    S3_PREFIX = os.getenv('S3_PREFIX', '')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    OUTPUT_PREFIX = os.getenv('OUTPUT_PREFIX', 'fairness-reports/')
    CHECK_INTERVAL_SECONDS = int(os.getenv('CHECK_INTERVAL_SECONDS', '43200'))
