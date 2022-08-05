from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def level1():
    return render_template("index.html", row = 8, col = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:row>')
def level2(row):
    return render_template("index.html", row = row, col = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:row>/<int:col>')
def level3(row, col):
    return render_template("index.html", row = row, col = col, color1 = 'red', color2 = 'black')

@app.route('/<int:row>/<int:col>/<color1>')
def level4(row, col, color1):
    return render_template("index.html", row = row, col = col, color1 = color1, color2 = 'black')

@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def level5(row, col, color1, color2):
    return render_template("index.html", row = row ,col = col ,color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)