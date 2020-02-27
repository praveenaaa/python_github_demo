'''
Created on Feb 25, 2020

@author: pravin.a.kumar.singh
'''
from selenium import webdriver
from select import select
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome("C:\driver99999\CHROME\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
driver.find_element_by_link_text("SignUp").click()
driver.find_element_by_name("userName").send_keys("pravin")
driver.find_element_by_id("firstName").send_keys("singh")
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//img[@alt='Ch']").click()
select1=Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select1.select_by_visible_text('May')
select2=Select(driver.find_element_by_xpath("//select[@data-handler='selectYear']"))
select2.select_by_visible_text('1957')
driver.find_element_by_xpath("//a[contains(.,'28')]").click()
select = Select(driver.find_element_by_name('securityQuestion'))

select.select_by_visible_text('What is your favour color?')
time.sleep(2)
select.select_by_value("411012")







