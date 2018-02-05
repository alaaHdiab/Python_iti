from vow import vow

from calc import calc 
                                                 
from str_index import str_index
      
from test import ff
                                                      
from dic import dic


import unittest

class TestAssignmentOne(unittest.TestCase):
    
    def test_vow(self):
        self.assertEqual(vow('mobile'), 'mbl')
        self.assertEqual(vow('MOBILE'), 'MBL')
        self.assertEqual(vow('MobIlE'), 'Mbl')
        
     
    def test_calc(self):
        self.assertEqual(calc('s',5,1),25)
        self.assertEqual(calc('r',3,4),12)
        self.assertEqual(calc('c',2,1),12.56)
        self.assertEqual(calc('t',12,6),36.0)
        
    
    
    def tes_tstr(self):
        self.assertEqual(str_index('This is javaScript','i'), [2,5,15])
    
    
    def test_tes(self):
        self.assertEqual(ff(3), [[1],[2,4],[3,6,9]])
        

    

    def test_dic(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(dic(l1), d1)
    
if __name__ == '__main__':
    unittest.main()
