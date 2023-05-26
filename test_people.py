try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '../src'
            )
        )
    )
except ImportError:
    raise


import unittest
from unittest.mock import patch
from src.people import People


class TestPeople(unittest.TestCase):
    def setUp(self):
        self.person = People("Hector", "Leubeck")

    def test_people_attr_name_has_the_correct_value(self):
        self.assertEqual(self.person.name, "Hector")

    def test_people_name_is_str(self):
        self.assertIsInstance(self.person.name, str)

    def test_people_attr_surname_has_the_correct_value(self):
        self.assertEqual(self.person.surname, "Leubeck")

    def test_people_surname_is_str(self):
        self.assertIsInstance(self.person.name, str)

    def test_people_attr_data_has_false(self):
        self.assertFalse(self.person.data)

    def test_people_connect_in_api_OK(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.person.connect_in_api(), "CONNECTED")
            self.assertTrue(self.person.data)

    def test_people_connect_in_api_error_404(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.person.connect_in_api(), "ERRO 404")

    def test_people_connect_in_api_false_positive(self):
        with patch("requests.get") as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.person.connect_in_api(), "CONNECTED")
            self.assertTrue(self.person.data)
            fake_request.return_value.ok = False

            self.assertEqual(self.person.connect_in_api(), "ERRO 404")


if __name__ == "__main__":
    unittest.main(verbosity=2)
