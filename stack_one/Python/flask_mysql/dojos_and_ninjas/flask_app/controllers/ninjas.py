from flask_app import app
from flask import render_template,redirect,request,Flask
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def create_ninja_html():
    return render_template('ninjas.html', dojos = Dojo.get_all_dojos())


@app.route('/create_ninjas', methods = ['POST'])
def create_ninja():

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/dojos')