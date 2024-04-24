import os

import allure
from dotenv import load_dotenv

from page_objects.create_ticket_page_obj import NewTicket
from page_objects.login_page_obj import LoginScreenObject
from page_objects.priority_page_obj import CreatePriority
from page_objects.status_page_obj import CreateStatus
from page_objects.ticket_page_obj import TicketScreen
from utilities.driverhandlers import DriverHandlers
from utilities.otp import retrieve_otp_from_email

load_dotenv()


@allure.feature('Test Scenario 1,2 and 3')
def test_sce_1_2_3(driver):
    try:
        driver.get("https://interview2.supporthive.com/staff/login")

        # login and retrieve OTP from email

        login = LoginScreenObject(driver)
        login.username_and_password_login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
        login.wait_for_resend_otp_button()
        driver.execute_script("window.open('https://mail.google.com/','_blank');")
        driver.switch_to.window(driver.window_handles[1])
        email_otp = retrieve_otp_from_email(driver)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        login.enter_otp(email_otp)
        login.final_login()

        # create status and make it default
        num = 928
        status_name = "Status"+str(num)
        priority_name = "Priority"+str(num)
        ticket_subject = "Ticket"+str(num)

        status_screen = CreateStatus(driver)
        status_screen.create_status(status_name)
        status_screen.make_newly_created_status_default(status_name)

        # create priority and make it default

        priority_screen = CreatePriority(driver)
        priority_screen.create_priority(priority_name)
        priority_screen.make_newly_created_priority_default(priority_name)

        # Create New Ticket

        driver.execute_script("window.open('https://interview2.supporthive.com/new/','_blank');")
        driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        assert driver.title == "New Ticket - Tenmiles - powered by HappyFox"
        create_ticket_screen = NewTicket(driver)
        create_ticket_screen.enter_subject(ticket_subject)
        create_ticket_screen.enter_message("Message")
        create_ticket_screen.enter_full_name("Mohamed Ashiq")
        create_ticket_screen.enter_email("mohdashiq996@gmail.com")
        create_ticket_screen.enter_phone("1234567890")
        create_ticket_screen.create_ticket()
        success_text = create_ticket_screen.ticket_creation_confirmation_message().get_attribute("textContent")
        assert success_text == "Your ticket has been created and you have been emailed instructions to activate your " \
                               "account with which you can track your ticket status"
        driver.switch_to.window(driver.window_handles[0])

        driver.refresh()
        ticket_screen = TicketScreen(driver)
        ticket_screen.hover_manage()
        ticket_screen.open_all_tickets()

        # check newly created ticket status and priority

        ticket_screen.view_created_ticket(ticket_subject)
        ticket_status = ticket_screen.get_ticket_status()
        assert ticket_status == status_name

        ticket_priority = ticket_screen.get_ticket_priority()
        assert ticket_priority == priority_name

        # Reply to ticket using canned action

        ticket_screen.click_reply()
        ticket_screen.click_canned_actions()
        ticket_screen.double_click_reply_to_customer_query()
        value = ticket_screen.values_in_editor()
        assert value == "Sample Canned Action Content"
        status = ticket_screen.get_ticket_status_inside_editor()
        assert status.strip() == "shipment"
        status = ticket_screen.get_ticket_priority_inside_editor()
        assert status.strip() == "Critical"
        tags = ticket_screen.get_ticket_tags_inside_editor()
        assert tags.strip() == "3 Tags"
        ticket_screen.click_add_reply()
        success_text_visible_check = ticket_screen.success_text()
        assert success_text_visible_check

        # Delete Status and Priority

        driver.get("https://interview2.supporthive.com/staff/manage/statuses")
        status_screen.view_ticket(status_name)
        status_screen.delete_link()
        status_screen.choose_category()
        status_screen.delete_button()
        status_screen.delete_confirmation()

        driver.get("https://interview2.supporthive.com/staff/manage/priorities")
        priority_screen.view_ticket(priority_name)
        priority_screen.delete_link()
        priority_screen.choose_category()
        priority_screen.delete_button()
        priority_screen.delete_confirmation()

        # logout

        login.logout()

    except Exception as e:
        DriverHandlers(driver).allure_exception(e)
