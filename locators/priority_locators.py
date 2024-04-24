from locators.status_locators import StatusLocators


class PriorityLocators:
    add_priority_video = "button[data-test-id='button-inside-popover']"
    new_priority = "button[data-test-id='new-priority']"
    priority_name = "input[data-test-id='form-field-name']"
    description = "textarea[data-test-id='form-field-description']"
    add_priority = "button[data-test-id='add-priority']"
    agent_help_text = "textarea[data-test-id='form-field-helpText']"
    delete_link = "a[data-test-id='priority-delete-trigger']"
    delete_button = StatusLocators.delete_button
    choose_status = "//span[text()='Choose Priority']/.."
    first_status = "//ul/li[1]"
