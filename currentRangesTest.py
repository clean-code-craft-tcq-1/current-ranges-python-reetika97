import unittest
import currentRanges

class CurrentRangesTest(unittest.TestCase):
  def test_count_min(self):
    self.assertTrue(currentRanges.count_min([4,4,5,5,4,8]) == [4,3])
  def test_remove_min(self):
    self.assertTrue(currentRanges.remove_min([4,4,5,5,4,8]) == [5,5,8])
  def test_def_range_count(self):
    self.assertTrue(currentRanges.def_range_count([4,4,5,5,4,8]) == [5,{4:5}])
  def test_def_all_ranges(self):
    range_count=[]
    ans= [[4, {4: 5}], [3, {8: 10}]]
    range_count=currentRanges.def_all_ranges([4,4,5,4,8,9,10],range_count)
    self.assertTrue(range_count == ans )
    
  def test_remove_min_listNotEmpty(self):
    self.assertFalse(currentRanges.remove_min([]) == [])
   
if __name__ == '__main__':
  unittest.main()
