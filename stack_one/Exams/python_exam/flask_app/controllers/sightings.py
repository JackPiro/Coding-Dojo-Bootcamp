from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.sighting import Sighting

@app.route('/dashboard')
def show_all_sightings():
    if 'user_id' not in session:
        print('user_id not in session, you have been redirected')
        return redirect('/')
    data = {
        'user_id' : session['user_id']
    }
    return render_template('home_page.html', sightings = Sighting.get_all_sightings(), user = User.get_user_by_id(data))


@app.route('/create_sighting_page')
def create_sighting_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id' : session['user_id']
    }
    return render_template('/create_sighting.html', user = User.get_user_by_id(data))


@app.route('/create_sighting', methods= ['POST'])
def create_sighting():
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        return redirect('/create_sighting_page')
    data = {
        'what_happened' : request.form['what_happened'],
        'location' : request.form['location'],
        'date_sighted' : request.form['date_sighted'],
        'number_of_squatches' : request.form['number_of_squatches'],
        'user_id' : session['user_id']
    }
    Sighting.create_sighting(data)
    return redirect('/dashboard')

@app.route('/delete_sighting/<int:sighting_id>', methods= ['POST'])
def delete_sighting(sighting_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'sighting_id' : sighting_id
    }
    Sighting.delete_sighting(data)
    return redirect('/dashboard')


@app.route('/edit_sighting_page/<int:sighting_id>')
def edit_sighting_page(sighting_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'sighting_id' : sighting_id,
        'user_id' : session['user_id']
    }
    return render_template('/edit_sighting.html', sighting = Sighting.get_sighting_by_id(data), user = User.get_user_by_id(data))


@app.route('/edit_sighting/<int:sighting_id>', methods=['POST'])
def edit_sighting(sighting_id):
    if 'user_id' not in session:
        return redirect('/')
    if not Sighting.validate_sighting(request.form):
        return redirect(f'/edit_sighting_page/{sighting_id}')
    data = {
        'sighting_id' : sighting_id,
        'what_happened' : request.form['what_happened'],
        'location' : request.form['location'],
        'date_sighted' : request.form['date_sighted'],
        'number_of_squatches' : request.form['number_of_squatches'],
    }
    Sighting.edit_sighting(data)
    return redirect('/dashboard')


@app.route('/view_sighting_page/<int:sighting_id>')
def view_sighting_page(sighting_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'sighting_id' : sighting_id,
        'user_id' : session['user_id']
    }
    return render_template('view_sighting.html', sighting = Sighting.get_sighting_by_id(data), user = User.get_user_by_id(data))