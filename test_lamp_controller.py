import unittest

from controllers import LampController

class TestLampController(unittest.TestCase):
    def test_turn_on(self):
        controller = LampController()
        controller.turn_on()
        self.assertTrue(controller.is_on())
    
    def test_turn_off(self):
        controller = LampController()
        controller.turn_off()
        self.assertFalse(controller.is_on())
    
    def test_turn_off_after_turn_on(self):
        controller = LampController()
        controller.turn_on()
        controller.turn_off()
        self.assertFalse(controller.is_on())

if __name__ == "__main__":
    unittest.main()