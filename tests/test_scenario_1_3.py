import allure

from page_objects.login_page_obj import LoginScreenObject
import os
from dotenv import load_dotenv

from page_objects.priority_page_obj import CreatePriority
from page_objects.status_page_obj import CreateStatus
from utilities.driverhandlers import DriverHandlers
from utilities.otp import retrieve_otp_from_email

load_dotenv()


@allure.feature('Test Scenario 1 and 3')
def test_scenario_1_and_3_create_and_delete_status_and_priority(driver):
    try:
        num = 1123
        status_name = 'Issue Created'+str(num)
        priority_name = "Assistance required"+str(num)

        driver.get("https://interview2.supporthive.com/staff/")

        login = LoginScreenObject(driver)

        # login and retrieve OTP from email

        login.username_and_password_login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
        login.wait_for_resend_otp_button()
        driver.execute_script("window.open('https://mail.google.com/','_blank');")
        driver.switch_to.window(driver.window_handles[1])
        email_otp = retrieve_otp_from_email(driver)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        login.enter_otp(email_otp)
        login.final_login()

        # create and delete Status

        status_screen = CreateStatus(driver)
        status_screen.create_status(status_name)
        status_screen.view_ticket(status_name)
        status_screen.delete_link()
        status_screen.delete_button()
        status_screen.delete_confirmation()

        # Create and delete Priority

        priority_screen = CreatePriority(driver)
        priority_screen.create_priority(priority_name)
        priority_screen.view_ticket(priority_name)
        priority_screen.delete_link()
        priority_screen.delete_button()
        priority_screen.delete_confirmation()

        login.logout()

    except Exception as e:
        DriverHandlers(driver).allure_exception(e)




