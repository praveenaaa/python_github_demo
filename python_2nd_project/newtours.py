import unittest
from selenium import webdriver


class Test(unittest.TestCase):


    def setUp(self):
     self.driver=webdriver.Chrome("C:\driver99999\chromedriver.exe")
     self.driver.maximize_window()
     self.driver.get("http://demo.guru99.com/test/newtours/")
     self.driver.implicitly_wait(1000)
     pass
    
    def tearDown(self):
     self.driver.close()
     pass


    def test_sign_on_mercury_tours(self):
     self.driver.find_element_by_name("userName").send_keys("mercury")
     self.driver.find_element_by_name("password").send_keys("mercury")
     self.driver.find_element_by_name("submit").click() 
     self.assertEqual(self.driver.title, "Login: Mercury Tours")
     print("succesfull")
    pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)
    
    
    