from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.index import index



# App Configuration
app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

# DB Configuration
db = SQLAlchemy(app)

# Routes
app.register_blueprint(index)


if __name__ == "__main__":
    app.run()
