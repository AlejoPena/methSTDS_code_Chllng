import unittest
import flat_list
import random
from flat_list import recoursive_flat
#from flat_list import rappend


class Test_flater(unittest.TestCase):

    def test_list(self):
        listt=[[1,2],[3,4],[5,6],[7,8],[9,10]]
        testlist=[]
        flat_list.recoursive_flat(listt, testlist)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_w_no_int(self):
        listt=[['a'],[3,4],[5,6],['random'],[1,['2','3','4'],1,'2'],[7,8],[9,10]]
        testlist=[]
        flat_list.recoursive_flat(listt, testlist)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_w_floats(self):
        listt=[[1],[1.3],[2,3,[4]],[5,6],[2.3333],[1.3,[[6.3]]],1.3, 0.3,[7,8],[9,10]]
        testlist=[]
        flat_list.recoursive_flat(listt, testlist)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_w_empties(self):
        listt=[[1],[[[[]]],[[[]]]],[2,3,[],],[5,6],[[]],[1,[],3,[[[]]]],[7,[],8],[9,10]]
        testlist=[]
        flat_list.recoursive_flat(listt, testlist)
        ##print(testlist)
        self.assertEqual(len(testlist), 11)

    def test_dicts(self):
        listt=[[1,[{2:3,4:5,5:6}],2],[3,4],[5,6],[7,8],[9,10]]
        testlist=[]
        flat_list.recoursive_flat(listt, testlist)
        ##print(testlist)
        self.assertEqual(len(testlist), 10)

    def test_big(self):
        listt=[]
        testlist=[]
        app_calls=0


        def rappend(lisa,calls):
            calls+=1
            rando=random.randint(0,1)
            if rando == 1:
                lis=[[],[],[]]
                calls+=rappend(lis[random.randint(0,2)],0)
                lisa.append(lis)
                
            else:
                ranto=random.randint(1,5)
                for i in range(ranto):
                    lisa.append(random.randint(1,99))
                calls+=(ranto-1)
            return calls

        for k in range(10000000):
            app_calls+=rappend(listt, 0)

        flat_list.recoursive_flat(listt, testlist)

        self.assertLess(len(testlist), app_calls)
        


if __name__ == '__main__':
    unittest.main()
