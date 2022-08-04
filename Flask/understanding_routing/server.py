from flask import Flask , render_template

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return render_template('index.html') 


    
@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/hello/<string:banana>/<int:num>') 
def hello(banana, num):
    return render_template('hello.html', banana = banana, num = num)

@app.errorhandler(404)
def error_page(e):
    return "my custom error page"

@app.route('/repeat/<num>/<text>') 
def show_user_profile(num, text):
    return int(num) * str(text)



# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

