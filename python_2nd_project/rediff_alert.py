from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver=webdriver.Chrome("C:\chromedriver.exe")
#driver=webdriver.Ie("C:\IEDriverServer.exe")
driver = webdriver.Chrome("C:\chromedriver.exe")
# driver=webdriver.Ie("C:\IEDriverServer.exe")

# Navigate to the application home page
driver.get("http://www.rediff.com/")
time.sleep(2)
driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_name("proceed").click()
time.sleep(2)
obj = driver.switch_to.alert


#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()


print(" Clicked on the OK Button in the Alert Window")
# al = driver.switch_to.alert()
# print (al.text)
# al.accept()
driver.close()


