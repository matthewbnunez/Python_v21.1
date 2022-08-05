from flask import Flask , render_template , session, redirect, request
app = Flask(__name__)    
app.secret_key = 'a secret key'

@app.route('/')
def play():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

# Increases the count by 1 by redirecting to the base page
@app.route("/count", methods=["POST"])
def plus_1():
    return redirect('/')

@app.route("/count2", methods=["POST"])
def plus_2():
    session['count'] += 1
    return redirect('/')
    
# Resets to count to 0
@app.route('/destroy_session', methods=["POST"])
def destroy():
    session.pop('count')
    return redirect('/')

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
