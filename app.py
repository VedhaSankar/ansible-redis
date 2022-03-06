from flask import Flask, render_template
import redis

# connect to redis
client = redis.Redis(host='localhost', port=6379)
app = Flask(__name__)

@app.route('/')
def start():
    
    # set a key
    client.set('test-key', 'test-value')

    # get a value
    value = client.get('test-key')
    print(type(value))

    return render_template('index.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)