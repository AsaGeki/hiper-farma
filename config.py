import os
import psycopg2
from dotenv import load_dotenv
import boto3

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")


def get_db_connection():
    try:
        db_connection = psycopg2.connect(
            host=str(DB_HOST),
            database=str(DB_NAME),
            user=str(DB_USER),
            password=str(DB_PASS),
            port=str(DB_PORT)
        )
        return db_connection
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None
    
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv("S3_REGION")
S3_KEY = os.getenv("AWS_ACCESS_KEY_ID")
S3_SECRET = os.getenv("AWS_SECRET_ACCESS_KEY")

def get_s3_client():
    try:
        s3_client = boto3.client(
            's3',
            region_name=S3_REGION,
            aws_access_key_id=S3_KEY,
            aws_secret_access_key=S3_SECRET
        )
        return s3_client
    except Exception as e:
        print("Erro ao criar cliente S3:", e)
        return None
