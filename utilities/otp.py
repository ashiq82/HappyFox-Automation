import os
import time

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


def retrieve_otp_from_email(driver):
    email = os.getenv("GMAIL_USERNAME")
    password = os.getenv("GMAIL_PASSWORD")
    driver.find_element(By.ID, "identifierId").send_keys(email)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    time.sleep(5)
    driver.refresh()
    element = driver.find_element(By.XPATH, "//span[text()='Your OTP (One-Time Password) for logging into HappyFox']")
    driver.execute_script("arguments[0].click()", element)
    otp = driver.find_element(By.XPATH, "(//b)[last()]").get_attribute("textContent")
    return otp
