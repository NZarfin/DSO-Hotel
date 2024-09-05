import click
import mysql.connector
import os

from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if "db" not in g or not g.db.is_connected():
        # connect to the database
        g.db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
            
            #ssl_ca = os.getenv("DB_SSL_CA")
            
        )
        
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        # close the database 
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
