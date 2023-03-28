from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/home')
def show_all_recipes():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    return render_template('home_page.html', recipes = Recipe.get_all_recipes(), users = User.get_user_by_id(data))



@app.route('/create_recipe_page')
def create_recipe_page():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_recipe.html')




@app.route('/save_recipe', methods= ['POST'])
def save_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/create_recipe_page')
    data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_cooked' : request.form['date_cooked'],
        'under_30' : request.form['under_30'],
        'user_id' : session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/home')




@app.route('/edit_recipe_page/<int:recipe_id>')
def edit_recipe_page(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id' : recipe_id
    }
    return render_template('edit_recipe.html', recipe = Recipe.get_recipe_by_id(data))




@app.route('/edit_recipe/<int:id>', methods=['POST'])
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_cooked' : request.form['date_cooked'],
        'under_30' : request.form['under_30']
    }
    Recipe.edit_recipe(data)
    return redirect('/home')

@app.route('/delete_recipe/<int:id>', methods = ['POST'])
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : id
    }
    Recipe.delete_recipe(data)
    return redirect('/home')

@app.route('/view_recipe_page/<int:id>')
def view_recipe(id):
    data = {
        'recipe_id' : id
    }
    Recipe.get_recipe_by_id(data)
    return render_template('view_recipe.html', recipe = Recipe.get_recipe_by_id(data))