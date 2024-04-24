import time

from selenium.webdriver.common.by import By

from locators.manage_list_locators import ManageLocators
from locators.ticket_locators import TicketObjects
from utilities.driverhandlers import DriverHandlers


class TicketScreen:
    def __init__(self, driver):
        self.driver = driver
        self.driver_handler = DriverHandlers(self.driver)

    def hover_manage(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ManageLocators.manage)
        self.driver_handler.move_to_element(element)

    def open_all_tickets(self):
        self.driver.find_element(By.XPATH, TicketObjects.tickets).click()

    def view_created_ticket(self, ticket_name):
        self.driver.find_element(By.XPATH, "//a[text()='" + ticket_name + "'][1]").click()
        self.driver.find_element(By.CSS_SELECTOR, TicketObjects.reply)

    def click_reply(self):
        self.driver.find_element(By.CSS_SELECTOR, TicketObjects.reply).click()
        self.driver_handler.wait_for_element_to_be_visible(25, (By.CSS_SELECTOR, TicketObjects.markdown))

    def click_canned_actions(self):
        self.driver.find_element(By.CSS_SELECTOR, TicketObjects.canned_action).click()

    def double_click_reply_to_customer_query(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, TicketObjects.reply_to_customer).click()
        assert self.get_preview_text() is not None
        element = self.driver.find_element(By.XPATH, TicketObjects.reply_to_customer)
        self.driver_handler.double_click(element)

    def click_use_this(self):
        self.driver_handler.wait_for_element_to_be_clickable(20, (By.CSS_SELECTOR, TicketObjects.use_this))
        self.driver.find_element(By.CSS_SELECTOR, TicketObjects.use_this).click()

    def get_preview_text(self):
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.preview_text)
        preview_text = element.get_attribute("textContent")
        return preview_text

    def click_add_reply(self):
        self.driver.find_element(By.CSS_SELECTOR, TicketObjects.add_reply).click()

    def values_in_editor(self):
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.editor_values)
        return element.get_attribute("textContent")

    def get_reply_count(self):
        self.driver_handler.wait_for_element_to_be_visible(25, (By.XPATH, TicketObjects.added_reply))
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.all_updates_view)
        count = (element.get_attribute("textContent")).strip()
        return int(count[5])

    def success_text(self):
        element = self.driver.find_element(By.XPATH, TicketObjects.success_text)
        return element.is_displayed()

    def get_ticket_status(self):
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.ticket_status)
        ticket_status = element.get_attribute("textContent")
        return ticket_status

    def get_ticket_priority(self):
        element = self.driver.find_element(By.XPATH, TicketObjects.ticket_priority)
        ticket_priority = element.get_attribute("textContent")
        return ticket_priority

    def get_ticket_status_inside_editor(self):
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.status_inside_editor)
        status = element.get_attribute("textContent")
        return status

    def get_ticket_priority_inside_editor(self):
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.priority_inside_editor)
        priority = element.get_attribute("textContent")
        return priority

    def get_ticket_tags_inside_editor(self):
        element = self.driver.find_element(By.CSS_SELECTOR, TicketObjects.tags_inside_editor)
        tags = element.get_attribute("textContent")
        return tags
