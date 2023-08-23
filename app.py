from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p style="font-size:16px; font-family:Verdana">Hello, World from a Docker Container!<p>'

@app.route('/<query>')
def show_query(query):
    return f'You are looking a path: {query}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
