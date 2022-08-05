from flask import Flask , render_template , session, redirect, request
app = Flask(__name__)    
app.secret_key = 'a secret key'

@app.route('/')
def play():
    return render_template('index.html')


@app.route("/process", methods=["POST"])
def processing():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    # users = [
    #     {'first_name': 'Michael', 'last_name': 'Choi'},
    #     {'first_name': 'John', 'last_name': 'Supsupin'},
    #     {'first_name': 'Mark', 'last_name': 'Guillen'},
    #     {'first_name': 'KB', 'last_name': 'Tonel'}
    # ]
    return redirect("/result")


@app.route("/result")
def display():
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('results.html', name=name, location=location, language=language, comment=comment)
    

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.