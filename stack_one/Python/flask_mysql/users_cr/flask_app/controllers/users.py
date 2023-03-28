# burgers.py
from flask_app import app
from flask import render_template,redirect,request,Flask
from flask_app.models.user import User


@app.route('/')
def users():
    return render_template("results.html", users = User.get_all() )


@app.route('/create')
def render_create():
    return render_template('create.html')

@app.route('/create_user', methods= ["POST"])
def create_user():

    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email']
    }
    if not User.validate_user(request.form):
        return redirect('/create')
    User.save(data)
    return redirect('/')

@app.route('/delete_user', methods= ['POST'])
def delete_user_route():
    User.delete_user(request.form)
    return redirect('/')

@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    data = {
        'user_id' : user_id
    }
    user = User.get_by_id(data)
    return render_template('edit_user.html', the_user_we_are_editing = user)


@app.route('/edit_user_route', methods= ['POST'])
def edit_user_route():
    data = {
    'id' : request.form['id'],
    'fname' : request.form['fname'],
    'lname' : request.form['lname'],
    'email' : request.form['email']
    }

    User.edit_user(data)
    return redirect('/')