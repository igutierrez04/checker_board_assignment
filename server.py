from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board_one():
    return render_template('index.html', col=8, row=8, color1= 'red', color2 = 'black')

@app.route('/<int:row>')
def board_two(row):
    return render_template('index.html', col=8, row = row, color1 ='red', color2='black')

@app.route('/<int:row>/<int:col>')
def board_tree(row, col):
    return render_template('index.html', col=col, row = row, color1 ='red', color2='black')

@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def board_four(row,col,color1,color2):
    return render_template('index.html', col=col, row = row, color1= color1, color2= color2)

if __name__=="__main__":
    app.run(debug=True)