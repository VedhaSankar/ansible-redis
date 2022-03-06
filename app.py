from flask import Flask, render_template, request
import redis
import random

# connect to redis
client = redis.Redis(host = 'redis', port = 6379, decode_responses = True)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():

    if request.method == 'POST':

        first_name  = request.values.get("fname")
        second_name = request.values.get("sname")

        # check if the user is already in the database
        if client.exists(f"{first_name}_{second_name}"):

            return render_template('index.html', data = client.get(f"{first_name}_{second_name}"))

        elif client.exists(f"{second_name}_{first_name}"):

            return render_template('index.html', data = client.get(f"{second_name}_{first_name}"))

        else:

            random_number = random.randint(1, 100)
            client.set(f"{first_name}_{second_name}", random_number)
            return render_template('index.html', data = random_number)


    return render_template('index.html')



@app.route('/test')
def test():
    
    # set a key
    client.set('test-key', 'test-value')

    # get a value
    value = client.get('test-key')
    print(value)

    return render_template('index.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)