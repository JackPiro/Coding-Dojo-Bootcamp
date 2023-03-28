from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/play/<int:num_rows>/<int:num_columns>')
def chess(num_rows,num_columns):
    if num_rows or num_columns < 2:
        return('requires at least two rows and columns.')
    else:
        return render_template('index.html', num_rows = num_rows, num_columns = num_columns)

if __name__=="__main__":
    app.run(debug=True)
