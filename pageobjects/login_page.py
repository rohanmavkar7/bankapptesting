from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Class:
    text_username_xpath="//input[@id='username']"
    text_password_xpath="//input[@id='password']"
    clickloginbutton= "//button[@id='loginButton']"
    clicklogoutbutton= "//a[normalize-space()='Logout']"


    def __init__(self,driver):
        self.driver = driver

    def EnterUserName(self,name):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(name)


    def UserPassword(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def ClickLogoutButton(self):
        self.driver.find_element(By.XPATH,self.clicklogoutbutton).click()

    def ClickLoginButton(self):
            self.driver.find_element(By.XPATH, self.clickloginbutton).click()
            try:
                self.driver.find_element(By.XPATH, self.clickloginbutton)
                return "login pass"
            except:
                return "login fail"






