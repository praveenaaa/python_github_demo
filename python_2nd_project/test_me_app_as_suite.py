import unittest
import HtmlTestRunner
from selenium import webdriver 
from time import sleep
import time
import select
from selenium.webdriver.support.select import Select
from python_2nd_project.hdfc_window_frame import GoogleOrgSearch1
class test_me_app2(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome("C:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8099/TestMeApp")
#         self.driver.find_element_by_link_text("SignIn").click()
#         sleep(2000)
        self.driver.implicitly_wait(1000)
        pass


    def tearDown(self):
        self.driver.close()
        pass


    def test_Sign_vin_testmeapp(self):
     self.driver.find_element_by_link_text("SignIn").click()
     self.driver.find_element_by_name("userName").send_keys("admin")
     self.driver.find_element_by_name("password").send_keys("password456")
     self.driver.find_element_by_name("Login").click() 
     self.assertEqual(self.driver.title, "Admin Home")
     print("admin login succesfull")
     self.driver.find_element_by_link_text("SignOut").click()
     time.sleep(3)
     pass

    def test_Sign_up_test_me_app(self):
     self.driver.find_element_by_link_text("SignUp").click()
     self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("pravin")
     self.driver.find_element_by_xpath("//input[@name='firstName']").send_keys("pravin")
     self.driver.find_element_by_xpath("//input[@name='lastName']").send_keys("singh")
     self.driver.find_element_by_xpath("//input[@value='Male']").click()
     self.driver.find_element_by_xpath("//input[@name='dob']").send_keys("03/03/1982")
#     s1=Select(driver.find_element_by_name("passCount"))
# s1.select_by_index(2)
# s2=Select(driver.find_element_by_name("fromPort"))
# s2.select_by_visible_text("Portland")
# s3=Select(driver.find_element_by_name("fromMonth"))
# s3.select_by_value("2")
     s1=Select(self.driver.find_element_by_name("securityQuestion"))
     
     time.sleep(2)
#      s1.select_by_value("411011")
     s1.select_by_visible_text("What is your favour color?")
     time.sleep(3)
     print("sign_up")
    
    def test_Sign_in_testmeapp1(self):
     self.driver.find_element_by_link_text("SignIn").click()
     self.driver.find_element_by_name("userName").send_keys("lalitha")
     self.driver.find_element_by_name("password").send_keys("password123")
     self.driver.find_element_by_name("Login").click() 
     self.assertEqual(self.driver.title, "Home")
     print("lalitha login succesfull")
     self.driver.find_element_by_link_text("SignOut").click()
     time.sleep(3)
     pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
# suite = unittest.TestLoader().loadTestsFromTestCase(test_me_app2)

# suite = unittest.TestLoader().loadTestsFromTestCase(GoogleOrgSearch1)  r8 now don't uncomment it 
# unittest.TextTestRunner(verbosity=3).run(suite)

