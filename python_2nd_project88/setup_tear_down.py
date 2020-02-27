'''
Created on Nov 13, 2018

@author: shweta.kushwaha
'''
import unittest


class Test(unittest.TestCase):

    @classmethod
    def setUpclass(self):
        print("hi setup")
        pass

    @classmethod
    def tearDownclass(self):
        print("hi teardown")
        pass


    def test_Name(self):
        print("test1")
        pass

    def test_Name2(self):
        print("test2")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
