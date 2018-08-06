import os
from flask import Flask
from redis import Redis
import psycopg2

app = Flask(__name__)

redis = Redis(host='redis', port=6379)

@app.route('/api')
def hello():
    redis.incr('hits')
    return '%s' % os.environ

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
