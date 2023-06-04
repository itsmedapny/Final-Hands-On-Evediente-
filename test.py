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

    # Insert Into Test 
    def test_payment(self):
        data = {
            "customerNumber": 103,
            "checkNumber": "H5677890",
            "paymentDate": "2004-10-20",
            "amount": 2500.00
        }
        response = self.app.post("/payments", json=data) 
        self.assertEqual(response.status_code, 201) # Found

    def test_payment(self):
        data = {
            "customerNumber": 500,
            "checkNumber": "H5789009",
            "paymentDate": "2021-10-20",
            "amount": 56789.00
        }
        response = self.app.post("/payments", json=data)
        self.assertEqual(response.status_code, 404) # Not Found 
    
    # Update statement test using put method
    def test_updatepayment(self):
        data = {
            "checkNumber": "LF501133",
            "amount": 250000
        }
        response = self.app.put("/payments/496", json=data)
        self.assertEqual(response.status_code, 200) # Found

    def test_updatepayment(self):
        data = {
            "checkNumber": "LGH1569",
            "amount": 16789.00
        }
        response = self.app.put("/payments/496", json=data)
        self.assertNotEqual(response.status_code, 404) # Not Found
 
    # Delete Statement test using delete method

    def test_delete(self):
        response = self.app.delete("/payments/H569067")
        self.assertEqual(response.status_code, 200) # Found 

    def test_deletenon(self):
        response = self.app.delete("/payments/143")
        self.assertNotEqual(response.status_code, 404)  # Not Found

if __name__ == "__main__":
    unittest.main()