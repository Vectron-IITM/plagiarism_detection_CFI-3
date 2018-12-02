__author__ = "Suyash Soni"
__email__ = "suyash.soni248@gmail.com"

import json
from flask_restful import Api
from settings import app, config
from mysql_connector import db

app.url_map.strict_slashes = False
api = Api(app)

def initialize_sqlalchemy():
    """ Initializes MySQL database connection. """

    config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(
        **config['MYSQL_DB_CONFIG']['URI_CONFIG']
    )

    config['MYSQL_CONNECTION_POOL_SIZE'] = config['MYSQL_DB_CONFIG']['MYSQL_CONNECTION_POOL_SIZE']
    config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['DEBUG']
    config['SQLALCHEMY_ECHO'] = config['DEBUG']
    config['SQLALCHEMY_RECORD_QUERIES'] = config['DEBUG']
    db.init_app(app)

    # For creating the tables(via models) for the first time.
    # import model
    # app.app_context().push()
    # db.create_all()

initialize_sqlalchemy()

# Registering routes.
from routes import register_urls
register_urls(api)

@app.route("/")
def index():
    return json.dumps({"message": "Welcome to Plagiarism Detector"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)


