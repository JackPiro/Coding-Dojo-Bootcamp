from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import dojo

@app.route('/dojos')
def show_dojos():
    return render_template('dojos.html', dojos = dojo.Dojo.get_all_dojos() )

@app.route('/create_dojo', methods = ['POST'])
def create_dojo():

    data = {
        'dojo_name' : request.form['dojo_name']
        # 'id' : request.form['id']
    }
    dojo.Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/delete_dojo/<int:id>')
def delete_dojo(id):

    data = {
        'id' : id
    }
    dojo.Dojo.delete_dojo(data)
    return redirect('/dojos')

@app.route('/dojos_ninjas/<int:id>')
def view_dojo(id):
    data = {
        'id' : id
    }
    return render_template('show_ninjas_from_dojo.html', dojo = dojo.Dojo.get_dojos_with_ninjas(data))
    


