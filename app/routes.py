from flask import Blueprint, render_template, request, redirect, flash
from config import get_db_connection, get_s3_client, S3_BUCKET

main = Blueprint('main', __name__)
workers = Blueprint('workers', __name__)
add_roles = Blueprint('add_roles', __name__)
add_workers = Blueprint('add_workers', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@workers.route('/workers', methods=['GET'])
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
    cursor.close()
    connect.close()
    return render_template('worker_list.html', worker_list = worker_list)

@add_roles.route('/add_role', methods=['POST'])
def add_role():
    connect = get_db_connection()
    cursor = connect.cursor()
    role = request.form['role'].lower().strip()
    cursor.execute('''
                   INSERT INTO roles(name)
                   VALUES ('%s')
                   ''', role)
    cursor.close()
    connect.close()
    return redirect('/workers')

@add_workers.route('/add_worker', methods=['POST'])
def add_worker():
    db = get_db_connection()
    s3 = get_s3_client()
    cursor = db.cursor()
    image = request.file.get('image')
    max_size_image = 5 * 1024 * 1024
    safe_formats_image = {'PNG', 'JPG'}
    
    if not image:
        flash('Arquivo obrigatório', 'error')
        
        
    
    
    
    
    
    
    
    
    first_name = request.form['first_name'].lower().strip()
    last_name = request.form['last_name'].lower().strip()
    cpf = request.form['cpf'].lower().strip()
    
    hiring_date = request.form['hiring_date']
    operation = request.form['operation'].lower().strip()
    contact = request.form['contact'].lower().strip()
    worker_role = request.form['worker_role'].lower().strip()
    gender = request.form['gender'].lower().strip()
    cursor.execute('''
                   INSERT INTO worker (first_name, last_name, cpf, picture, hiring_date, 
                   operation, contact, worker_role, gender)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,)
                   ''', )

