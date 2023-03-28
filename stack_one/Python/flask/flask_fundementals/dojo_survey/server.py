from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "we did it"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def create_user():
    print('got post info')
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['dojo_location']
    session['language'] = request.form['fave_language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('show.html')

@app.route('/reset')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)