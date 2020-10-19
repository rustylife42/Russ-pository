import unittest
import assign_average


class MyTestCase(unittest.TestCase):
    def testA(self):
        self.assertEqual(assign_average.switch_average('A'), 100)

    def testB(self):
        self.assertEqual(assign_average.switch_average('B'), 101)

    def testC(self):
        self.assertEqual(assign_average.switch_average('C'), 102)

    def testD(self):
        self.assertEqual(assign_average.switch_average('D'), 103)

    def testE(self):
        self.assertEqual(assign_average.switch_average('E'), 104)

    def testF(self):
        self.assertEqual(assign_average.switch_average('F'), 105)

    def testWrong(self):
        self.assertFalse(assign_average.switch_average('Z').isnumeric())


if __name__ == '__main__':
    unittest.main()
