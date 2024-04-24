from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.driverhandlers import DriverHandlers
from utilities.logger import log
from locators.new_ticket_locators import NewTicketLocators


class NewTicket:
    def __init__(self, driver):
        self.driver = driver
        self.driver_handlers = DriverHandlers(self.driver)

    def enter_subject(self, subject):
        element = self.driver.find_element(By.ID, NewTicketLocators.subject)
        element.send_keys(subject)
        log().info(f"Entered Subject {subject}")

    def enter_message(self, message):
        self.driver_handlers.wait_for_element_to_be_visible(15, (By.CSS_SELECTOR, NewTicketLocators.message))
        element = self.driver.find_element(By.CSS_SELECTOR, NewTicketLocators.message)
        action = ActionChains(self.driver)
        action.click(on_element=element).send_keys(message).perform()
        log().info(f"Entered Message {message}")

    def enter_full_name(self, full_name):
        element = self.driver.find_element(By.ID, NewTicketLocators.full_name)
        element.send_keys(full_name)
        log().info(f"Entered Full Name {full_name}")

    def enter_email(self, email):
        element = self.driver.find_element(By.ID, NewTicketLocators.email)
        element.send_keys(email)
        log().info(f"Entered Email {email}")

    def enter_phone(self, phone):
        element = self.driver.find_element(By.ID, NewTicketLocators.phone)
        element.send_keys(phone)
        log().info(f"Entered Phone Number {phone}")

    def create_ticket(self):
        element = self.driver.find_element(By.ID, NewTicketLocators.create_ticket)
        element.click()

    def ticket_creation_confirmation_message(self):
        self.driver_handlers.wait_for_element_to_be_visible(40, (By.CSS_SELECTOR, NewTicketLocators.confirmation_text))
        return self.driver.find_element(By.CSS_SELECTOR, NewTicketLocators.confirmation_text)

