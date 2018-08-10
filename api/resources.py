from .db import get_db
from flask import Response
from flask_restful import Resource
import json

class HelloResource(Resource):
    '''
    A simple JSON API endpoint
    '''
    def get(self):
        db = get_db()
        cur = db.cursor()

        cur.execute('select * from test;')

        def generate():
            for row in cur.fetchall():
                (pk, msg) = row
                return json.dumps({
                    'pk': pk,
                    'msg': msg
                })
            cur.close()

        return Response(generate(),mimetype='application/json')
