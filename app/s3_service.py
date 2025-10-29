from flask import current_app

def get_s3_file_url(filename):
    bucket = current_app.config['S3_BUCKET']
    region = current_app.config['S3_REGION']
    return f"https://{bucket}.s3.{region}.amazonaws.com/{filename}"
