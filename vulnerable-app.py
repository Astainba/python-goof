import os
import subprocess
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/run', methods=['POST'])
def run_command():
    # 🚨 Command Injection via untrusted input
    user_input = request.form['input']
    cmd = f"echo {user_input}"  # Snyk will flag this line
    output = subprocess.check_output(cmd, shell=True)
    return output

@app.route('/file', methods=['GET'])
def read_file():
    # 🚨 Arbitrary File Read
    filename = request.args.get('name')
    with open(filename, 'r') as f:
        return f.read()

@app.route('/env')
def show_env():
    # 🚨 Information disclosure
    return str(dict(os.environ))

if __name__ == '__main__':
    app.run(debug=True)
