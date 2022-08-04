from flask import Flask , render_template # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/hello/<string:banana>/<int:num>')  # for a route '/users/____/____', two parameters in the url get passed as username and id
def hello(banana, num):
    return render_template('hello.html', banana = banana, num = num)

@app.route('/repeat/<num>/<text>') 
def show_user_profile(num, text):
    return int(num) * str(text)

@app.errorhandler(404)
def error_page(e):
    return "my custom error page"

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.