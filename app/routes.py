from flask import Blueprint, render_template
from config import get_db_connection, get_s3_client, S3_BUCKET

main = Blueprint('main', __name__)
workers = Blueprint('workers', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@workers.route('/workers')
def workers_list():
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('''
                   SELECT w.cpf, w.first_name || ' ' || w.last_name AS nome_completo, d.department_name
                   FROM worker w
                   JOIN department_worker dw ON w.worker_id = dw.worker_id
                   JOIN department d ON d.department_id = dw.department_id
                   ''')
    worker_list = cursor.fetchall()
    connect.close()
    cursor.close()
    return render_template('worker_list.html', worker_list = worker_list)


