from flask import Blueprint, render_template, request, redirect, flash
from config import get_db_connection, get_s3_client, S3_BUCKET
from PIL import image

add = Blueprint('add', __name__)
add_worker = Blueprint('add_worker', __name__)

def validation(field_value: str, field_label: str) -> bool:
    if not field_value:
        flash(f"O Campo {field_label} é obrigatório.")
        return False
    return True

@add.route('/add')
def add_pag():
    return render_template('add.html')

@add_worker.route('/add/worker', methods=['POST'])
def add_worker_route():
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
    
    validations = [
        validation(first_name, 'Primeiro Nome'),
        validation(last_name, 'Sobrenome'),
        validation(cpf, 'CPF'),
        validation(hiring_date, 'Data de Contratação'),
        validation(operation, 'Atividade'),
        validation(worker_role, 'Função'),
        validation(gender, 'Gênero')
    ]
    if not all(validations):
        return redirect('/add/worker')
    
    cursor.execute('''
                   INSERT INTO worker (first_name, last_name, cpf, picture, hiring_date, 
                   operation, contact, worker_role, gender)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,)
                   ''', )
    
    cursor.close()
    db.close()
    s3.close()
    flash("Cadastro feito com sucesso")
    return redirect('/add')

    