
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
# Import the Flask class from the flask_app module and create an instance of the Flask class

# Import the Bcrypt class from the flask_bcrypt module and create an instance of the Bcrypt class
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def users():
    return render_template("login.html", users = User.get_all() )

@app.route('/home')
def logged_in_user():
    data = {
        'id' : session['user_id']
    }
    return render_template("home_page.html", users = User.get_user_by_id(data))

@app.route('/create_user', methods= ["POST"])
def create_user():


    if not User.validate_user(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' : request.form['email'],
        'hashed_password' : hashed_password
    }
    one_user = User.save(data) #use this user object to access the user id
    session['one_user'] = one_user
    return redirect('/home')



# Define a route that handles POST requests to the /login URL
@app.route('/login_user', methods=['POST'])
def login():
    # Get the email and password provided by the user from the request form
    data = { "email" : request.form["email"] }
    
    # Use the User.get_by_email() method to see if the user with the provided email exists in the database
    user_in_db = User.get_user_by_email(data)
    
    # If the user does not exist in the database, display an error message and redirect the user to the login page
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
        
    # If the user does exist in the database, verify the provided password using the bcrypt.check_password_hash() method
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # If the password is not correct, display an error message and redirect the user to the login page
        flash("Invalid Email/Password")
        return redirect('/')
        
    # If the password is correct, set the user's id in the session and redirect the user to the dashboard page
    session['user_id'] = user_in_db.id
    return redirect("/home")
