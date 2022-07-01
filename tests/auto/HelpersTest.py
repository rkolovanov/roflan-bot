from roflan_bot.helpers import get_random_element
import unittest


class HelpersTest(unittest.TestCase):
    def test_get_random_element(self):
        self.assertRaises(ValueError, lambda: get_random_element([]))

        test_list = [1, "2", 3.4, 5]
        for i in range(10):
            self.assertTrue(get_random_element(test_list) in test_list)
