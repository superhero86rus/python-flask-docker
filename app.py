from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    log("Requesting main page!")
    return '<p style="font-size:16px; font-family:Verdana">Hello, World from a Docker Container!<p>'

@app.route('/<query>')
def show_query(query):
    log("Another request: " + query)
    return f'You are looking a path: {query}'

def log(msg):
    file=open("logs/requests.log", "a+")
    file.write(msg + "\n")
    file.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

