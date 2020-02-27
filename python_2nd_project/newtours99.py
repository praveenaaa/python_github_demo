'''
Created on Feb 25, 2020

@author: pravin.a.kumar.singh
'''

from selenium import webdriver

from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome("C:\driver99999\CHROME\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_link_text("REGISTER").click()
driver.find_element_by_name("firstName").send_keys("pravin")

driver.find_element_by_name("lastName").send_keys("pravin")
select=Select(driver.find_element_by_name("country"))
select.select_by_visible_text("INDIA")
driver.find_element_by_name("submit").click()






