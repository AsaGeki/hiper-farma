from config import get_db_connection, get_s3_client

def name_bagde(first_name, last_name):
    if ' ' in first_name:
        return first_name
    else:
        last_word = last_name.split(' ')[-1]

        complete_name = f'{first_name} {last_word}'
        return complete_name
    


def add_worker():
    db = get_db_connection()
    s3 = get_s3_client()
    cursor = db.cursor()
    first_name = request
    cursor.execute('''
                   INSERT INTO worker (first_name, last_name, cpf, picture, hiring_date, 
                   operation, contact, worker_role, gender)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,)
                   ''', )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



 s3 = get_s3_client()
    image_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': S3_BUCKET, 'Key':'teste.jpg'},
    ExpiresIn=3600
    )
    return render_template('index.html', worker=worker, image=image_url)