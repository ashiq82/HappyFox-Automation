import time

from selenium.webdriver.common.by import By

from locators.manage_list_locators import ManageLocators
from locators.priority_locators import PriorityLocators
from utilities.driverhandlers import DriverHandlers


class CreatePriority:
    def __init__(self, driver):
        self.driver = driver
        self.driver_handler = DriverHandlers(self.driver)

    def hover_manage(self):

        self.driver_handler.wait_for_element_to_be_visible(20, (By.CSS_SELECTOR, ManageLocators.manage))
        element = self.driver.find_element(By.CSS_SELECTOR, ManageLocators.manage)
        self.driver_handler.move_to_element(element)

    def priority_from_list(self):
        return self.driver.find_element(By.CSS_SELECTOR, ManageLocators.priorities)

    def new_priority(self):
        return self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.new_priority)

    def priority_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.priority_name)

    def priority_description(self):
        return self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.description)

    def agent_help_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.agent_help_text)

    def add_priority(self):
        return self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.add_priority)

    def wait_for_new_priority_to_be_created(self, name):
        element = self.driver.find_element(By.CSS_SELECTOR, "span[title='" + name + "']")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def make_newly_created_priority_default(self, name):
        try:
            status_check = self.driver.find_element(By.XPATH, "//tr[last()]/td[2]/span")
            element = self.driver.find_element(By.XPATH, "//tr[last()]/td[5]")
            title = status_check.get_attribute("title")
            if title == name:
                self.driver_handler.move_to_element(element)
                self.driver.find_element(By.XPATH, "//tr[last()]/td[5]//div[@class='hf-make-default']").click()
                self.driver.find_element(By.XPATH, "//tr[last()]/td[5]//div[@data-test-id='default-priority']")
            else:
                raise ValueError("Newly created Priority is not visible")
        except Exception as e:
            raise ValueError(e)

    def delete_link(self):
        self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.delete_link).click()

    def delete_button(self):
        self.driver.find_element(By.CSS_SELECTOR, PriorityLocators.delete_button).click()

    def view_ticket(self, ticket_name):
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, "span[title='" + ticket_name + "']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.click()

    def choose_category(self):
        self.driver.find_element(By.XPATH, PriorityLocators.choose_status).click()
        self.driver.find_element(By.XPATH, PriorityLocators.first_status).click()

    def delete_confirmation(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.hf-toast-message_text")

    def create_priority(self, priority_name):
        self.hover_manage()
        self.priority_from_list().click()
        self.new_priority().click()
        self.priority_name().send_keys(priority_name)
        self.priority_description().send_keys("Priority of the newly created tickets")
        self.add_priority().click()
        self.wait_for_new_priority_to_be_created(priority_name)
