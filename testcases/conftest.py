

import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="class")
def setup(request):
        browser_value = request.config.getoption("--browser")
        if browser_value == "chrome":
            print("launching in chrome")
            driver = webdriver.Chrome()
        elif browser_value == "firefox":
            print("launching in firefox")
            driver = webdriver.Firefox()
        elif browser_value == "headless":
            print("launching headless browser")
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.maximize_window()
#        driver.get("https://apps.credence.in/") #link closed after creating readconfig file
        request.cls.driver= driver
        yield driver
        driver.quit()
