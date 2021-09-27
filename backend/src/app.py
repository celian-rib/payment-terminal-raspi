import os

from flask import Flask
from api import api
from database.database import init_db
from backup import check_if_backup_required

check_if_backup_required()

if __name__ == '__main__':
    app = Flask(__name__)

    api.init_app(app)
    init_db()

    if os.environ.get('PROD') == None :
        app.run(debug=True)
    else :
        app.run(debug=False, port=5000, host="0.0.0.0")
