from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")
window_before1 = driver.window_handles[0]
         
print(window_before1) 
title1=driver.title
print(title1)
#          driver.find_element_by_xpath("//a[https://twitter.com]").click()
driver.switch_to.frame(1)
driver.find_element_by_xpath("//a[contains(.,'Privacy Policy')]").click()
#          
print("========clicked on privacy policy====")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
privacy_title=driver.title
print(privacy_title)
driver.find_element_by_link_text("Personal").click()
print("clicked on personal link ")
#          driver.switch_to.default_content()
driver.switch_to.window(window_before1)
time.sleep(2)
driver.switch_to.frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("444378")
time.sleep(2)
driver.quit()
         
#          