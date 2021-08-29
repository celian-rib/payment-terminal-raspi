from flask import Flask
from api import api
from database.database import init_db

app = Flask(__name__)
api.init_app(app)
init_db()

if __name__ == '__main__':
    app.run(debug=True)
