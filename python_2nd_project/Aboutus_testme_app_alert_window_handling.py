'''
Created on Feb 27, 2020

@author: pravin.a.kumar.singh
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
driver.maximize_window()
window_before1 = driver.window_handles[0]

about_us = driver.find_element_by_link_text("AboutUs")
ourOffice = driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/a/span")
chennaiLocation = driver.find_element_by_xpath("//*[@id='menu3']/li[3]/ul/li/ul/li[1]/a/span")

action1 = ActionChains(driver)
action1.move_to_element(about_us).move_to_element(ourOffice).move_to_element(chennaiLocation).click(chennaiLocation).perform()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.switch_to_frame("main_page")
contactUs = driver.find_element_by_id("demo3").text

print(contactUs)

driver.quit()
