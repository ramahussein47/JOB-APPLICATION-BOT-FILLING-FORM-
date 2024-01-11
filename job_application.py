from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
# Set up the webdriver
driver = webdriver.Chrome()

# Open Instagram
driver.get("https://instagram.com/")

# Locate username and password fields and login button, then fill in your credentials
username_input =driver.find_element(By.CLASS_NAME,'_ab32')
username_input.send_keys("craejag675@gmail.com")
password_input=driver.find_element(By.CLASS_NAME,'_ab32')

password_input.send_keys("mhbbLL!q1eAJtlS")

password_input=driver.find_element(By.CLASS_NAME,'_ab32')

password_input.send_keys(Keys.RETURN)


time.sleep(30)


