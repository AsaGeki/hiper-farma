from flask import Flask, render_template, request, redirect
from config import get_connection


app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM worker ORDER BY id_client ASC;''')
    worker = cur.fetchall()
    cur.close()
    conn.close()
    s3_file = https://asageki.s3.sa-east-1.amazonaws.com/teste.jpg
    return render_template('index.html', worker=worker, s3_file=s3_file)
