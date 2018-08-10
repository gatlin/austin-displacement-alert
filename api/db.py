from flask import g, current_app
import os
import psycopg2
from flask.cli import with_appcontext
import click
import json

def get_db():
    '''
    Get (and create, if necessary) an app-global database connection.
    '''
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASS'),
            host='postgres' # defined in the docker env file
        )
    return g.db

def close_db(db=None):
    '''
    Clean up the database connection.
    '''
    if not db:
        db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    '''
    Performs any crucial initialization steps on the database.
    '''
    db = get_db()
    with db:
        with db.cursor() as cur:
            cur.execute('create extension pgcrypto;')

@click.command('init-db')
@with_appcontext
def init_db_command():
    '''
    Clear the existing data and create new tables.
    This will be registered as a flask command.
    '''
    init_db()
    click.echo('Initialized the database')

def init_app(app):
    '''
    Register the database connection with the app's lifecycle.
    '''
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
