from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "we did it"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods = ['POST'])
def create_user():
    print('got post info')
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user_data():
    print('showing user data')
    print(request.form)
    return render_template('show.html')

if __name__=="__main__":
    app.run(debug=True)