from flask import Flask , render_template

app = Flask(__name__)    

@app.route('/')
def play():
    return 'Hello World'
    
@app.route('/play')
def level1():
    return render_template('index.html', num = 3)

@app.route('/play/<int:num>') 
def level2(num):
    return render_template('index.html', num = num)

@app.route('/play/<int:num>/<color>') 
def level3(color, num):
    return render_template('index.html', num = num, color = color)

# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

