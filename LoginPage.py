from selenium.webdriver.common.by import By
class LoginPage():
    #Locators of all elements
    textbox_username_id= "Email"
    textbox_password_id= "password"
    button_login_xpath= "//*[@class='button-1 login-button']"
    link_logout_linktext= "Log out"
    def __init__(self,driver) :    # Ceate constructor to initialize the driver
        self.driver=driver
        # For Every Element we need to create an action method
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click
