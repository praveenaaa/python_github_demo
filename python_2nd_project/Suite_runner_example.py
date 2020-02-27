#suiterunnerexample 

import unittest

import HtmlTestRunner
from HtmlTestRunner.runner import HTMLTestRunner


class SampleTest(unittest.TestCase):
    def test_pass(self):
        """Test to demonstrate pass condition"""
        self.assertTrue(True)        

    def test_fail(self):
        """Test to demonstrate fail condition"""
        self.assertFalse(False)
    def test_faim(self):
        """Test to demonstrate fail condition"""
        self.assertFalse(True)
def suite():
    s1 = unittest.TestLoader().loadTestsFromTestCase(SampleTest)
    return unittest.TestSuite([s1])


if __name__ == "__main__":  
    unittest.main()
    
#     testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\python_practice99\\python__2nd_project\\python_2nd_project\\reports')



