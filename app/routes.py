from flask import Blueprint, render_template
from config import get_connection
from app.s3_service import get_s3_file_url  # função que retorna a URL do S3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM worker ORDER BY id_client ASC;')
    worker = cur.fetchall()
    cur.close()
    conn.close()

    s3_file = get_s3_file_url("teste.jpg")
    return render_template('index.html', worker=worker, s3_file=s3_file)
