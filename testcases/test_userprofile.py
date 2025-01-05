import random
import string
import pytest
import faker
from selenium.webdriver.common.by import By

from pageobjects.SignUp_Page import SignUp_class
from pageobjects.login_page import Login_Class
from utilities.Logger_utility import logger_class
from utilities.additional_utilities import additional_utilities_class
from utilities.readConfig_utility import readconfig_class


@pytest.mark.usefixtures("setup")
class Test_login01:
    username = readconfig_class.username_data()
    password = readconfig_class.password_data()
    base_url = readconfig_class.base_url()
    login_url = readconfig_class.login_url()
    signup_url = readconfig_class.signup_url()
    log = logger_class.log_gen_method()
    driver = None

    def test_Bankapp_login002(self):
        self.log.info("Testing Login")
        self.driver.get(self.login_url)
        self.log.info(f"Checking bank app title: {self.driver.title}")
        lp = Login_Class(self.driver)
        self.log.info("Entering username and password")
        lp.EnterUserName(self.username)
        self.log.info("Entering password")
        lp.UserPassword(self.password)
        lp.ClickLoginButton()
        self.log.info("Login button clicked")
        additional_utilities_class.explicit_wait(self.driver,By.XPATH,lp.clickloginbutton)
        print(f"Actual title: {self.driver.title}")
        if self.driver.title == "Dashboard":
            self.log.info("Test case passed: Login successful")
            print("Test case passed: Login successful")
            assert True
        else:
            self.log.info("Test case failed: Login failed")
            print("Test case failed: Login failed")
            assert False
    @pytest.mark.sanity
    @pytest.mark.userprofile
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_bankapp_url003(self):
        self.log.info("Testing URL")
        self.log.info(f"Base URL: {self.base_url}")
        self.driver.get(self.base_url)
        self.log.info(f"checking bank app title: {self.driver.title}")
        if self.driver.title == "Bank Application":
            self.log.info("Test case passed: URL working")
            self.log.info("Taking screenshot")
            #self.driver.save_screenshot(".\\Screenshots\\testurl_pass.png")  # For taking screenshots
            additional_utilities_class.take_screenshots(self.driver,"test_bankapp_url003","pass" )
            print("Test case passed: URL working")
            assert True
        else:
            self.log.info("Test case failed: URL not working")
            self.log.info("Taking screenshot")
            additional_utilities_class.take_screenshots(self.driver,"test_bankapp_url003","fail" )
            print("Test case failed: URL not working")
            assert False
        self.driver.quit()

    def test_SignUp_class004(self, faker):
        self.log.info("Testing SignUp")
        # Step 1: Open the signup page
        self.log.info("Opening the signup page")
        self.driver.get(self.signup_url)  # Target signup page URL
        self.log.info(f"Checking bank app title: {self.driver.title}")
        # Step 2: Initialize the SignUp_class object
        sp = SignUp_class(self.driver)  # Object for interacting with signup elements
        self.log.info("Filling in the signup form")
        # Step 3: Fill in the username
        sp.Enterusername("usernameFDFD15583")  # Static username for test

        # Step 4: Fill in the password
        sp.Enterpassword("sh64554@WW")  # Static password for test
        print("Entered password: ******")  # Masking the password output for security

        # Step 5: Generate and fill in the email
        email = faker.email()  # Generate a random email using Faker
        print(f"Generated email: {email}")
        sp.Enteremail(email)

        # Step 6: Generate and fill in the phone number
        phone_number = generate_random_phone_number()  # Generate random phone number
        print(f"Generated phone number: {phone_number}")
        sp.Enterphone(phone_number)

        # Step 7: Click the 'Create User' button
        sp.ClickCreateUserButton()
        print("Clicked on the 'Create User' button.")
        additional_utilities_class.explicit_wait(self.driver,By.XPATH,sp.success_msg_xpath)
        # Step 8: Verify the success message
        print(f"Actual title: {self.driver.title}")
        if sp.Verify_SuccessMessage() == "User created successfully":
            print("Test Passed: User signup was successful.")
            #self.driver.save_screenshot(r"C:\Users\Lenovo\Desktop\PYTHON\bankapp_pytest_dec\Screenshots\signup_screenshot.png")
            additional_utilities_class.take_screenshots(self.driver,"test_SignUp_class004","pass" )
            assert True
        else:
            #self.driver.save_screenshot(r"\Users\Lenovo\Desktop\PYTHON\bankapp_pytest_dec\Screenshots\signup_failure.png")
            additional_utilities_class.take_screenshots(self.driver,"test_SignUp_class004","fail" )
            print("Test Failed: User Not Created Successfully.")
            assert False


def generate_random_phone_number():  # Use for generating a 10-digit phone number
    return ''.join(random.choices(string.digits, k=10))
