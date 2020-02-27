from selenium import webdriver
import unittest
import time
import openpyxl
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common import by
from os import path
from _ast import For
import os


class Read_excel(unittest.TestCase):

      
     def test_readExcel(self): 
         self.driver = webdriver.Chrome("C:\chromedriver.exe")
         
         self.driver.get("http://localhost:8099/TestMeApp")
         self.driver.find_element_by_link_text("SignIn").click()
         self.driver.implicitly_wait(10)
         self.driver.maximize_window() 
         path = os.getcwd()
         print (path)
         
         wb=openpyxl.load_workbook('C:\\Users\\pravin.a.kumar.singh\\Desktop\\python_excel_data.xlsx')
#          sheet1=wb.get_sheet_by_name('sheet1')
         sheet1=wb['Sheet1']
         cells=sheet1['A2:B5']
         for c1,c2 in cells:
             self.test_login(c1.value,c2.value)   
             
         
     def test_login(self,username,password):
         self.driver.find_element_by_name("userName").send_keys(username)
         self.driver.find_element_by_name("password").send_keys(password)
         time.sleep(2)
         self.driver.find_element_by_name("Login").click()
         title=self.driver.title
         self.driver.find_element_by_partial_link_text("SignOut").click() 
         time.sleep(5)
         self.assertEqual(self.driver.title, "Home")
         title=self.driver.title
         print(title)
         time.sleep(4)
         self.driver.find_element_by_link_text("SignIn").click()
          
         
         
         def tearDown(self):
          self.driver.close()
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
     unittest.main()
#        
       