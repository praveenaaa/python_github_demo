'''
Created on Feb 26, 2020

@author: pravin.a.kumar.singh
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome("C:\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/droppable/");
driver.switch_to.frame(0)
sorc= driver.find_element_by_id("draggable")
tgt=driver.find_element_by_id("droppable")

        
actions = ActionChains(driver)

actions.drag_and_drop(sorc, tgt).perform()

      
