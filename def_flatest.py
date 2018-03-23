import unittest
import flat_list
import random
from flat_list import flatten_list
#from flat_list import rappend


class Test_flater(unittest.TestCase):

    def test_list(self):
        listt=[[1,2],[3,4],[5,6],[7,8],[9,10]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_empty(self):
        listt=[[],[]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 0)

    def test_w_no_int(self):
        listt=[['a'],[3,4],[5,6],['random'],[1,['2','3','4'],1,'2'],[7,8],[9,10]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_w_floats(self):
        listt=[[1],[1.3],[2,3,[4]],[5,6],[2.3333],[1.3,[[6.3]]],1.3, 0.3,[7,8],[9,10]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_w_empties(self):
        listt=[[1],[[[[]]],[[[]]]],[2,3,[],],[5,6],[[]],[1,[],3,[[[]]]],[7,[],8],[9,10]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 11)

    def test_dicts(self):
        listt=[[1,[{2:3,4:5,5:6}],2],[3,4],[5,6],[7,8],[9,10]]
        testlist=flat_list.flatten_list(listt)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

'''
    def test_big(self):
        listt=[]
        testlist=[]
        app_calls=0
        def rappend(lisa,calls):
            calls+=1
            rando=random.randint(0,1)
            if rando == 1:
                lis=[]
                calls+=rappend(lis,calls)
                lisa.append(lis)
                lisa.append(1)
            else:
                for i in range(random.randint(1,5)):
                    lisa.append(random.randint(1,99))
            return calls

        for k in range(50):
            app_calls+=rappend(listt, 0)

        laa=flat_list.flatten_list(listt, testlist)

        self.assertLess(len(testlist), app_calls)

'''

if __name__ == '__main__':
    unittest.main()
