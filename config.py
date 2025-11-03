import os
from dotenv import load_dotenv
import psycopg2
import boto3

load_dotenv()

# Conexão com a AWS PostgreSQL
def get_db_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None

# Cliente S3
def get_s3_client():
    try:
        return boto3.client(
            "s3",
            region_name=os.getenv("S3_REGION"),
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
        )
    except Exception as e:
        print("Erro ao criar cliente S3:", e)
        return None
