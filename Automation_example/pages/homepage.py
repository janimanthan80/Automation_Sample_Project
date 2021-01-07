from Automation_example.locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.driver_welcome_id = Locators.driver_welcome_id
        self.driver_logout_linktext = Locators.driver_logout_linktext

    def welcome_page(self):
        self.driver.find_element_by_id(self.driver_welcome_id).click()

    def perform_logout(self):
        self.driver.find_element_by_link_text(self.driver_logout_linktext).click()