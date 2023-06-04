import unittest
import warnings
import json
from flask import Flask
from api import app

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>Hello, World!</p>")

    # Select Statement Test
    def get_customers(self):
        response = self.app.get("/customers")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Schmitt" in response.data.decode()) # Found

    def get_customers(self):
        response = self.app.get("/customers")
        self.assertEqual(response.status_code, 404)
        self.assertTrue("Evediente" in response.data.decode()) # Not Found

    # Update Statement 

    def update_customers(self):
        response = self.app.get("/customers/update")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Philippines" in response.data.decode()) # Found
   
    def update_customers(self):
        response = self.app.get("/customers/update")
        self.assertEqual(response.status_code, 404)
        self.assertTrue("Manila" in response.data.decode()) # Not Found 


if __name__ == "__main__":
    unittest.main()