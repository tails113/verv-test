import connexion
import couchdb
import os

from flask import Flask
from flask.views import MethodView

from flask_injector import FlaskInjector

from injector import inject

from models import Product


app = connexion.FlaskApp(__name__, specification_dir='./')

app.add_api('swagger.yml')

couch_db = couchdb.Server(os.environ.get('DATABASE_URL'))


class ProductView(MethodView):

    @inject
    def __init__(self, db: couch_db):
        self.db = db

    def get(self, *args, **kwargs):        
        return 'test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
