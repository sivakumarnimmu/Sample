from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.makemytrip.com/flights/")
driver.maximize_window()
Round1=driver.find_element(By.CLASS_NAME, "selected")
print(Round1.is_selected())