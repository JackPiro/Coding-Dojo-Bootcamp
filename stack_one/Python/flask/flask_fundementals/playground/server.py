from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/success')
def success():
    return "success"
    # @app.route('/repeat/<int:num>/<word>')
# def hi_michael(num, word):
#     return render_template('hello.html', word = word, num = num)

@app.route('/users/<username>/<id>')
def show_users_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def say_flask(name):
    return f'HI {name}'


@app.route('/play')
def play_level_1():
    return render_template('index.html')

@app.route('/play/<int:num_boxes>')
def play_level_2(num_boxes):
    return render_template('index.html', num_boxes = num_boxes)

@app.route('/play/<int:num_boxes>/<string:color>')
def play_level_3(num_boxes, color):
    return render_template('index.html', num_boxes = num_boxes, color = color)


if __name__=="__main__":
    app.run(debug=True)
