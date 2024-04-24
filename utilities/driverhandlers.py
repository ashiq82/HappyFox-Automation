import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverHandlers:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(to_element=element).perform()

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(on_element=element).perform()

    def add_images_to_allure_report(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG,
        )

    def allure_exception(self, e):
        allure.attach(str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        self.add_images_to_allure_report("Failed Image")
        raise
