import main
import unittest

class TestChatBot(unittest.TestCase):
  def test_yesno(self):
    self.assertEqual(main.generate_response(1), "No") #Check if passing 1 to returns yes (one possible output)