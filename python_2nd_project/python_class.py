'''
Created on Feb 26, 2020

@author: pravin.a.kumar.singh
'''
from selenium import webdriver
from selenium.webdriver.common import keys
import time
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.switch_to_frame("login_page")

driver.find_element_by_name("fldLoginUserId").send_keys("444378")

driver.switch_to_default_content()
driver.switch_to_frame(1)
driver.find_element_by_link_text("Privacy Policy").click()