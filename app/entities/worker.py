from config import get_db_connection

def name_bagde(first_name, last_name):
    if ' ' in first_name:
        return first_name
    else:
        last_word = last_name.split(' ')[-1]

        complete_name = f'{first_name} {last_word}'
        return complete_name
    
def add_role(role):
    connect = get_db_connection()
    cursor = connect.cursor()
    cursor.execute('''
                   INSERT INTO roles(name)
                   VALUES ('%s')
                   ''', role)
    cursor.close()
    connect.close()

def add_worker():
    db = get_db_connection()
    s3 = 