from flask import Flask, send_file

app = Flask("test")

index = ""

@app.route("/click", methods=["POST"])
def click():
    return "<h1>YOU CLICKED THE BUTTON!</h1>"

@app.route('/', defaults={'req_path': 'index.html'})
@app.route('/<path:req_path>')
def index(req_path):
    return send_file(f"dist/{req_path}")

app.run()
