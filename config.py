import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")


def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None
    
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET")

def get_s3_config():
    return {
        "bucket": S3_BUCKET,
        "region": S3_REGION,
        "access_key": S3_KEY,
        "secret_key": S3_SECRET
    }
