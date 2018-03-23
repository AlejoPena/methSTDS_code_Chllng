import unittest
import temptracker
import random as ra

class Testpy(unittest.TestCase):


  def test_min(self):
    b=temptracker.TempTracker()
    lista=[28,34,55,67,23,29,58,67,58]
    for i in lista:
      b.insert(i)
    self.assertEqual(b.get_min(), 23)


  def test_max(self):
    b=temptracker.TempTracker()
    lista=[-28,-34,-55,67,23,29,58,67,58]
    for i in lista:
      b.insert(i)
    self.assertEqual(b.get_max(), 67)

  def test_tracker(self):
    a=temptracker.TempTracker()
    for i in range(10):
        a.insert(i)
    self.assertEqual(a.get_mean(), '4.50')


  def test_many(self):
    a=temptracker.TempTracker()
    for i in range(19999):
        a.insert(ra.randint(9,110))
    results=[19999,9,110]
    self.assertEqual(a.printall(), results)


  def test_empty(self):
    a=temptracker.TempTracker()
    self.assertNotEqual(type(a.get_min),type(1))
    self.assertNotEqual(type(a.get_max),type(1))
    self.assertNotEqual(type(a.get_mean),type(1))

if __name__ == '__main__':
  unittest.main()
