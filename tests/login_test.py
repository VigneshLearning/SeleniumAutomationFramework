import time

import allure
from selenium import webdriver
import pytest
from pages.pageToLogin import pageToLogin
from pages.pageToHome import pageToHome
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome("C://Users//Vignesh//PycharmProjects//Selenium//driver//chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     yield
    #     driver.close()
    #     driver.quit()
    #     print("Podu Thakida Thakida")

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        obj = pageToLogin(driver)
        obj.enter_username(utils.USERNAME)
        obj.enter_password(utils.PASSWORD)
        obj.click_login()
        time.sleep(2)

    def test_logout(self):
        try:
            driver = self.driver
            obj1 = pageToHome(driver)
            obj1.click_welcome()
            obj1.click_logout()
            x = driver.title
            assert x == "abc"
            # assert x == "OrangeHRM"
            time.sleep(3)

        except AssertionError as error:
            print("Assertion Error is occurred")
            print(error)
            testName = utils.whoami()
            allure.attach(self.driver.get_screenshot_as_png(),name=testName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Vignesh/PycharmProjects/AutomationFramework1/screenshots/"+ testName +".png")
            raise

        except:
            print("There was an exception")
            testName = utils.whoami()
            allure.attach(self.driver.get_screenshot_as_png(), name=testName,
                          attachment_type=allure.attachment_type.PNG)
            raise

        else:
            print("No Exception Occurred")

        finally:
            print("I'm inside the finally Block")


# We Can also have TRY and EXCEPT block here with RAISE keyword to get the Test Case Failed