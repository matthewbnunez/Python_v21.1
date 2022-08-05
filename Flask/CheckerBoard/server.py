from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", row = 8, col = 8, color1 = 'red', color2 = 'black')


@app.route('/<int:x>')
def row(row):
    return render_template("index.html", row = row, col = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>')
def row_col(row, col):
    return render_template("index.html", row = row, col = col, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<color1>')
def row_col_one(row, col, color1):
    return render_template("index.html", row = row, col = col, color1 = color1, color2 = 'black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def row_col_two(row, col, color1, color2):
    return render_template("index.html", row = row ,col = col ,color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)