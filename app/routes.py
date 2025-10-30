from flask import Blueprint, render_template
from config import get_db_connection, get_s3_client, S3_BUCKET

main = Blueprint('main', __name__)
@main.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM worker;')
    worker = cur.fetchall()
    cur.close()
    conn.close()
    s3 = get_s3_client()
    image_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': S3_BUCKET, 'Key':'teste.jpg'},
    ExpiresIn=3600
    )
    return render_template('index.html', worker=worker, image=image_url)
