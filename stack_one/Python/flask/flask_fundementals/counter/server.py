from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "we did it"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] = session['counter'] + 1
    return redirect('/count')

@app.route('/count')
def show_counter():
    return render_template('index.html')

@app.route('/reset')
def reset_count():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)