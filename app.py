from flask import Flask
from redis import Redis
import os
import socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def hello():
    redis.incr('global_hits')
    redis.incr(host)
    return 'Global: {global_hits}, Local: {local_hits}, host: {host}'.format(
        global_hits=redis.get('global_hits'),
        local_hits=redis.get(host),
        host=host
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
