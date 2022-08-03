from flask import Flask  

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  


    
@app.route('/dojo')
def success():
  return "Dojo!"

@app.route('/say/<name>') 
def hello(name):
    return "Hello, " + str(name)

@app.route('/repeat/<num>/<text>') 
def show_user_profile(num, text):
    return int(num) * str(text)



# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

