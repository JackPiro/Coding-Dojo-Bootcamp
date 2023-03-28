from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.author import Author
from flask import Flask, render_template, redirect, request



@app.route('/authors')
def create_author_page():
    return render_template('new_author_all_authors.html', authors = Author.get_all_authors())

@app.route('/create_new_author', methods= ['POST'])
def create_new_author():
    data = {
        'name' : request.form['name']
    }
    Author.create_author(data)
    return redirect('/authors')
