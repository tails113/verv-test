from flaskext.couchdb import Document
from flaskext.couchdb import (
    TextField,
    IntegerField
)


class Product(Document):
    doc_type = 'product'

    _id = TextField()
    prodname = TextField()
    catagory = TextField()
    quantity = IntegerField()

    def __repr__(self):
        return '<Product %r>' % self.prodname
