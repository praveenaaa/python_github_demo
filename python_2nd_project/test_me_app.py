import unittest
import HtmlTestRunner
from selenium import webdriver 
from time import sleep
import time
import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class test_me_app2(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome("C:\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:8099/TestMeApp")
#         self.driver.find_element_by_link_text("SignIn").click()
#         sleep(2000)
        self.driver.implicitly_wait(10)
        pass


    def tearDown(self):
        self.driver.close()
#         self.driver.quit()
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
#      menu=self.driver.find_element_by_link_text("All Categories")
#      submenu1=self.driver.find_element_by_link_text("Electronics")
#      submenu2=self.driver.find_element_by_link_text("Head Phone")
#      ActionChains(self.driver).move_to_element(menu).click(submenu1).click(submenu2).perform()
     
     
     self.driver.find_element_by_link_text("SignOut").click()
     time.sleep(3)
     pass
    
    def test_about_us(self):
     window_before1 = self.driver.window_handles[0]

     about_us = self.driver.find_element_by_link_text("AboutUs")
     ourOffice = self.driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/a/span")
     chennaiLocation = self.driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/ul/li[1]/a/span")

     action1 = ActionChains(self.driver)
     action1.move_to_element(about_us).move_to_element(ourOffice).move_to_element(chennaiLocation).click(chennaiLocation).perform()

     window_after = self.driver.window_handles[1]
     self.driver.switch_to.window(window_after)

     self.driver.switch_to_frame("main_page")
     contactUs = self.driver.find_element_by_id("demo3").text

     print(contactUs)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\python_practice_21st_feb\\python__2nd_project\\reports889'))
    
#     C:\python_practice99\python__2nd_project\reports99
    