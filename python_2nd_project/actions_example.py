from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("C:\driver99999\chromedriver.exe")

# driver=webdriver.Ie("C:\IEDriverServer.exe")
driver.get("http://localhost:8099/TestMeApp")

driver.maximize_window()

driver.implicitly_wait(1000)
driver.find_element_by_link_text("SignIn").click()
driver.find_element_by_name("userName").send_keys("lalitha")
driver.find_element_by_name("password").send_keys("password123")
driver.find_element_by_name("Login").click() 
print("lalitha login succesfull")
time.sleep(2)

#      menu=self.driver.find_element_by_link_text("All Categories")
#      submenu1=self.driver.find_element_by_link_text("Electronics")
#      submenu2=self.driver.find_element_by_link_text("Head Phone")
#      ActionChains(self.driver).move_to_element(menu).click(submenu1).click(submenu2).perform()
# menu1 = driver.find_element_by_link_text("All Categories")
menu1=driver.find_element_by_xpath("//*[@id='menu3']/li[2]/a/span")
sub_menu0 = driver.find_element_by_xpath("//*[@id='menu3']/li[2]/ul/li[1]/a/span")
sub_menu1=driver.find_element_by_xpath("//*[@id='submenuul11290']/li[1]/a/span")
#  clickon = drivers.find_element_by_xpath(path/of/option/where/you/want/to/click)
action = ActionChains(driver)
action.move_to_element(menu1)
action.move_to_element(sub_menu0)
action.click(sub_menu0)
action.move_to_element(sub_menu1)
action.click(sub_menu1)
action.perform()



