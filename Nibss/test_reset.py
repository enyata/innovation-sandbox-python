import unittest
import Nibss.request as RS


class MyTestCase(unittest.TestCase):
    def test_reset(self):
        self.assertEqual(RS.reset("MTExMTE=", "8dc1337c1ac82aa90f3bd7b8de8d882a"), 200, "should be 200")


if __name__ == '__main__':
    unittest.main()
