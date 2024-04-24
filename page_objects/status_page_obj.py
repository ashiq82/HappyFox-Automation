from selenium.webdriver.common.by import By

from locators.manage_list_locators import ManageLocators
from locators.status_locators import StatusLocators
from utilities.driverhandlers import DriverHandlers


class CreateStatus:
    def __init__(self, driver):
        self.driver = driver
        self.driver_handler = DriverHandlers(self.driver)

    def hover_manage(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ManageLocators.manage)
        self.driver_handler.move_to_element(element)

    def status_from_list(self):
        return self.driver.find_element(By.CSS_SELECTOR, ManageLocators.status)

    def new_status(self):
        self.driver_handler.wait_for_element_to_be_visible(20, (By.CSS_SELECTOR, StatusLocators.new_status))
        return self.driver.find_element(By.CSS_SELECTOR, StatusLocators.new_status)

    def status_name(self):
        self.driver_handler.wait_for_element_to_be_visible(20, (By.CSS_SELECTOR, StatusLocators.new_status))
        return self.driver.find_element(By.CSS_SELECTOR, StatusLocators.status_name)

    def status_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, StatusLocators.description)

    def add_status(self):
        return self.driver.find_element(By.CSS_SELECTOR, StatusLocators.add_status)

    def del_status(self):
        return self.driver.find_element(By.CSS_SELECTOR, StatusLocators.add_status)

    def wait_for_new_status_to_be_created(self, name):
        element = self.driver.find_element(By.CSS_SELECTOR, "div[title='" + name + "']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def make_newly_created_status_default(self, name):
        try:
            status_check = self.driver.find_element(By.XPATH, "//tr[last()]/td[2]/div/div")
            element = self.driver.find_element(By.XPATH, "//tr[last()]/td[5]")
            title = status_check.get_attribute("title")
            if title == name:
                self.driver_handler.move_to_element(element)
                self.driver.find_element(By.XPATH, "//tr[last()]/td[5]//a").click()
                self.driver_handler.wait_for_element_to_be_visible(15, (By.XPATH, "//tr[last()]/td[5]/div/div["
                                                                                  "@data-test-id='default-status']"))
            else:
                raise ValueError("Newly created element is not visible")
        except Exception as e:
            raise ValueError(e)

    def delete_link(self):
        self.driver.find_element(By.CSS_SELECTOR, StatusLocators.delete_link).click()

    def delete_button(self):
        self.driver.find_element(By.CSS_SELECTOR, StatusLocators.delete_button).click()

    def view_ticket(self, ticket_name):
        element = self.driver.find_element(By.CSS_SELECTOR, "div[title='" + ticket_name + "']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.click()

    def choose_category(self):
        self.driver.find_element(By.XPATH, StatusLocators.choose_status).click()
        self.driver.find_element(By.XPATH, StatusLocators.first_status).click()

    def delete_confirmation(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.hf-toast-message_text")

    def create_status(self, status_name):
        self.hover_manage()
        self.status_from_list().click()
        self.new_status().click()
        self.status_name().send_keys(status_name)
        self.status_description().send_keys("Status when a new ticket is created in HappyFox")
        self.add_status().click()
        self.wait_for_new_status_to_be_created(status_name)
