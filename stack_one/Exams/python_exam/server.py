from flask_app.controllers import users
from flask_app.controllers import sightings
from flask_app import app
from jinja2 import StrictUndefined

app.jinja_env.undefined = StrictUndefined

if __name__ == "__main__":
    app.run(debug=True)