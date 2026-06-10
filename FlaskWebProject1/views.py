"""
Routes and views for the flask application.
"""

import os
import mysql.connector
from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/time')
def get_mysql_time():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'mysql-db'),
            port=int(os.environ.get('DB_PORT', 3306)),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', 'secret'),
            database=os.environ.get('DB_NAME', 'mysql')
        )
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")
        db_time = cursor.fetchone()
        cursor.close()
        connection.close()
        return f"<h1>MySQL Current Time: {db_time[0]} from todays class (2nd of june 2026)</h1>"
    except Exception as e:
        return f"<h1>Error connecting to MySQL:</h1><p>{str(e)}</p>"
    
@app.route('/version')
def get_version():
    return {"version": "2.1"}