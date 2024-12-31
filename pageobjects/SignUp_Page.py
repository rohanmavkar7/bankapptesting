
from selenium.webdriver.common.by import By

class SignUp_class :
    text_username_xpath = "//input[@id='username']"
    text_password_xpath = "//input[@id='password']"
    text_email_xpath = "//input[@id='email']"
    text_phone_xpath = "//input[@id='phone']"
    click_create_user_button_ID="createUserButton"
    success_msg_xpath = "//div[@id='successMessage']"

    def __init__(self, driver):
        self.driver = driver

    def Enterusername(self, name):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(name)

    def Enterpassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def Enteremail(self, email):
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def Enterphone(self, phone):
        self.driver.find_element(By.XPATH, self.text_phone_xpath).send_keys(phone)

    def ClickCreateUserButton(self ):
        ClickCreateUserButton = self.driver.find_element(By.ID, self.click_create_user_button_ID)
        self.driver.find_element(By.ID, self.click_create_user_button_ID)
        self.driver.execute_script("arguments[0].scrollIntoView();", ClickCreateUserButton)
        ClickCreateUserButton.click()

    def Verify_SuccessMessage(self):
        try:
            msg = self.driver.find_element(By.XPATH, self.success_msg_xpath)
            print(msg.text)
            return "signup_pass"
        except:
            return "signup_fail"
