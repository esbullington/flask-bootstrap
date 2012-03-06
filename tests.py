import os
import unittest
import tempfile

from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        
        self.app = app.test_client()
        

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
