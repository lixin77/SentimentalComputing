from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    receive the uploaded file, and save it on the server
    :return:
    """
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/test.txt')


if __name__ == '__main__':
    app.run()
