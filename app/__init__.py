from flask import Flask
from config import get_connection
from flask import render_template


app = Flask(__name__)
conn = get_connection()
