# Import Flask to allow us to create our app
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/success')
def success():
    return "success <h1>this is a h1</h1><script>alert('hello!')</script>"


@app.route('/hello')
def hello():
    return render_template("index.html")


@app.route('/template')
def template():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("index.html", users=users)


@app.errorhandler(404)
def error_page(e):
    return "my custom error page"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
