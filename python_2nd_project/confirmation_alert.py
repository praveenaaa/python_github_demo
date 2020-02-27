from selenium import webdriver
from selenium.webdriver.common import keys
import time
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
location = "C:\\Users\\pravin.a.kumar.singh\\Desktop\\experiment\\confirmation_alert.htm"
driver.get(location)

#Click on the "Alert" button to generate the Confirmation Alert
button = driver.find_element_by_name('alert')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

#Section 1
#use the accept() method to accept the alert
obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)

time.sleep(2)

#refresh the webpage
driver.refresh()


# Section 2
# Re-generate the Confirmation Alert
button = driver.find_element_by_name('alert')
button.click()

time.sleep(2)

#Switch the control to the Alert window
obj = driver.switch_to.alert

# Dismiss the Alert using
obj.dismiss()

#get the text returned when Cancel Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)

driver.close





