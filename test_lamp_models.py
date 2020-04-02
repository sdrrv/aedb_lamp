import unittest
from models import ColorLamp

class TestLamp(unittest.TestCase):
    pass

class TestColorLamp(unittest.TestCase):
    def setUp(self):
        self.lamp = ColorLamp()

    def test_default_color(self):
        self.assertEqual(self.lamp.get_color(), 'White')

    def test_set_color(self):
        self.lamp.set_color('Black')
        self.assertEqual(self.lamp.get_color(), 'Black')

class TestLampArray(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()