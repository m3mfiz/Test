from flask import Flask, request, send_from_directory, redirect, url_for

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'secret'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if username == USERNAME and password == PASSWORD:
            return send_from_directory('.', 'success.html')
        else:
            # Invalid credentials, reload login page
            return send_from_directory('.', 'login.html'), 401
    return send_from_directory('.', 'login.html')

if __name__ == '__main__':
    app.run(debug=True)
