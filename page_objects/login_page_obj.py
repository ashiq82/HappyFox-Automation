import time

from utilities.driverhandlers import DriverHandlers
from utilities.logger import log
from locators.login_logout_locators import LoginScreen
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginScreenObject:
    def __init__(self, driver):
        self.driver = driver
        self.driver_handler = DriverHandlers(self.driver)

    def enter_user_name(self, name):
        element = self.driver.find_element(By.ID, LoginScreen.user_name)
        element.send_keys(name)
        log().info(f"Entered Username {name}")

    def enter_password(self, password):
        element = self.driver.find_element(By.ID, LoginScreen.password)
        element.send_keys(password)
        log().info(f"Entered Password {password}")

    def remember_me(self):
        return self.driver.find_element(By.ID, LoginScreen.remember_me)

    def wait_for_resend_otp_button(self):
        self.driver_handler.wait_for_element_to_be_visible(20, (By.ID, LoginScreen.resend_otp))

    def click_login(self):
        element = self.driver.find_element(By.ID, LoginScreen.login_button)
        element.click()

    def final_login(self):
        element = self.driver.find_element(By.CSS_SELECTOR, LoginScreen.final_login)
        element.click()

    def login_after_providing_otp(self):
        element = self.driver.find_element(By.CSS_SELECTOR, LoginScreen.final_login)
        element.click()

    def click_remember_me(self):
        element = self.driver.find_element(By.ID, LoginScreen.remember_me)
        element.click()

    def enter_otp(self, otp):
        element = self.driver.find_element(By.ID, LoginScreen.otp_input)
        element.send_keys(otp)
        log().info(f"Entered OTP - {otp}")

    def user_avatar(self):
        element = self.driver.find_element(By.CSS_SELECTOR, LoginScreen.user_avatar)
        element.click()

    def logout_button(self):
        element = self.driver.find_element(By.CSS_SELECTOR, LoginScreen.logout)
        element.click()

    def username_and_password_login(self, name, password):
        """Login with username and password and wait for mfa verification"""
        self.enter_user_name(name)
        self.enter_password(password)
        remember_me = self.remember_me().is_enabled()
        assert remember_me
        self.click_login()
        self.wait_for_resend_otp_button()

    def logout(self):
        self.user_avatar()
        self.logout_button()
        self.driver.find_element(By.XPATH, LoginScreen.logout_confirmation)
