from flask_testing import TestCase

from clikpik import app, db
from clikpik.microservicio import Producto


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Producto(nombre="productotest", ubicacion="ubicaciontest" ))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()