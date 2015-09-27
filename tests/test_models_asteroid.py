import unittest
from models.asteroid import Asteroid
from decimal import Decimal


class AsteroidTest(unittest.TestCase):
    """Test the implementation of the various utils functions"""
    sample_data = {
        "name": "Fake Asteroid",
        "number": "0000001",
        "designation": "0000001"
    }

    def test_name(self):
        """Test that an Asteroid's name is correctly set"""
        asteroid = Asteroid(self.sample_data)
        self.assertEqual(asteroid.name, 'Fake Asteroid')

    def test_number(self):
        """Test that an Asteroid's number is correctly set"""
        asteroid = Asteroid(self.sample_data)
        self.assertEqual(asteroid.number, "0000001")

    def test_designation(self):
        """Test that an Asteroid's designation is correctly set"""
        asteroid = Asteroid(self.sample_data)
        self.assertEqual(asteroid.designation, "0000001")
