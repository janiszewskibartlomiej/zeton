import sqlite3

from flask import current_app, g


def get_db():



def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
