from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initialize Chrome browser
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
#Open Browser
driver.get("https://www.makemytrip.com/")
#maximize Window
driver.maximize_window()
time.sleep(10)
Title=driver.title
print(Title) 
URL=driver.current_url
print(URL)
time.sleep(5)
driver.switch_to.alert.dismiss()
#driver.find_element(By.XPATH, "//*[@class='selected']").click()
time.sleep(10)