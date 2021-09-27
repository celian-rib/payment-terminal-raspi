import os

from flask import Flask
from api import api
from database.database import init_db
from backup import check_if_backup_required
from waitress import serve

if __name__ == '__main__':
    app = Flask(__name__)

    api.init_app(app)
    init_db()

    if os.environ.get('PROD') == None :
        # Development schema
        app.run(debug=True)
    else :
        # Production schema
        check_if_backup_required()
        print("App started in production")
        serve(app, port=5000, host="0.0.0.0")
