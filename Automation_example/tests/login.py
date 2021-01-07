from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Automation_example.pages.homepage import HomePage
from Automation_example.pages.loginpage import LoginPage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\MANTHAN\\PycharmProjects\\pythonProject\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_01login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.press_login_button()

        homepage = HomePage(self.driver)
        homepage.welcome_page()
        homepage.perform_logout()
        time.sleep(3)

    def test_02login_invalid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(self.driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.press_login_button()
        message = self.driver.find_element_by_xpath("").text
        self.assertEqual(message, "__Invalid Credentials__")

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/MANTHAN/PycharmProjects/pythonProject/Automation_example/Reports"))
