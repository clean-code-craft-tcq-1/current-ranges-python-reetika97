import unittest
import currentRanges

class CurrentRangesTest(unittest.TestCase):
  def test_count_min(self):
    self.assertTrue(count_min([4,4,5,5,4,8]) == [4,3])


if __name__ == '__main__':
  unittest.main()
