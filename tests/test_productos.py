import unittest

from flask import request

from tests.base import BaseTestCase
from clikpik import Producto



class TestProductos(BaseTestCase):


    def test_productos(self):
        result = self.client.get("/productos")
        print(result)
        self.assertEqual(result.status_code, 200)

        pass


if __name__ == '__main__':
    unittest.main()