import unittest
import main

class tester(unittest.TestCase):

    def test_bored_api(self):
        self.assertTrue(isinstance(main.get_activity(), main.activity_class))

    def test_DB_connection(self):
        db = main.DB_interface('tasks.db')
        db.list()