import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GoogleOrgSearch(unittest.TestCase):

     def setUp(self):
         self.driver = webdriver.Chrome("C:\chromedriver.exe")

     def test_google_search_page(self):
         driver = self.driver
         driver.get("https://www.facebook.com/")
         window_before1 = driver.window_handles[0]
         
         print(window_before1) 
         msg2=driver.title
         print(msg2)
#          driver.find_element_by_xpath("//a[https://twitter.com]").click()
         driver.find_element_by_xpath("//a[contains(.,'Instagram')]").click()
         msg1=driver.title
         print(msg1)
#          driver.find_element_by_xpath("//a[@href='https://instagram.com/']").click()
         window_after = driver.window_handles[1]
         driver.switch_to.window(window_after)
         print(window_after)
#          driver.find_element_by_link_text("ATM").click()
         driver.switch_to.window(window_before1)
         msg=driver.title
         print(msg)


     def tearDown(self):
          self.driver.close()

if __name__ == "__main__":
       unittest.main()


