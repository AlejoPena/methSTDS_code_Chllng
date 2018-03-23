import unittest
import pypro
import random as ra

class Testpy(unittest.TestCase):


  def test_min(self):
    b=pypro.TempTracker()
    lista=[28,34,55,67,23,29,58,67,58]
    for i in lista:
      b.insert(i)
    self.assertEqual(b.get_min(), 23)


  def test_max(self):
    b=pypro.TempTracker()
    lista=[-28,-34,-55,67,23,29,58,67,58]
    for i in lista:
      b.insert(i)
    self.assertEqual(b.get_max(), 67)

  def test_tracker(self):
    a=pypro.TempTracker()
    for i in range(10):
        a.insert(i)
    self.assertEqual(a.get_mean(), '4.50')


  def test_many(self):
    a=pypro.TempTracker()
    for i in range(19999999):
        a.insert(ra.randint(9,110))
    results=[19999999,9,110]
    self.assertEqual(a.printall(), results)


'''
  def test_empty(self):
    a=pypro.TempTracker()
    a.insert()
    self.assertEqual()
'''

if __name__ == '__main__':
  unittest.main()
