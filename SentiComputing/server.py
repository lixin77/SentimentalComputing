from flask import Flask, request, render_template, make_response, url_for, redirect

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    """
    redirect to the index page
    :return:
    """
    response = make_response(redirect('/index'))
    return response

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    receive the uploaded file, and save it on the server
    :return:
    """
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/test.txt')

@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    main page of the web application
    :return:
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
