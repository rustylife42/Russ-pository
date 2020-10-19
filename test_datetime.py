import unittest
from datetime import datetime, timedelta
import dateTime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        date = datetime(2020, 8, 5)
        self.assertEqual(dateTime.half_birthday(2020, 8, 5), date + timedelta(weeks=24))


if __name__ == '__main__':
    unittest.main()
