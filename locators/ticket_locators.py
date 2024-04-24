from locators.manage_list_locators import ManageLocators


class TicketObjects:
    manage = ManageLocators.manage
    tickets = "//div[text()='Tickets']"
    reply = "a[data-test-id='reply-link']"
    canned_action = "div.hf-floating-editor_toolbar-item div[class*='hf-popover-trigger']"
    reply_to_customer = "//li[text()='Reply to Customer Query']"
    use_this = "button[data-test-id='hf-add-canned-action']"
    preview_text = "div.hf-canned-action-preview>div>div"
    add_reply = "button[data-test-id='add-update-reply-button']"
    added_reply = "//div[@class='hf-update-box_body']//div[text()='Sample Canned Action Content']"
    all_updates_view = "div[data-test-id='all-updates-view']"
    editor_values = "div.cke_wysiwyg_div"
    markdown = "a.cke_button__markdown"
    success_text = "//div[text()='Ticket has been updated successfully']"
    ticket_status = "span.hf-update-activity_status"
    ticket_priority = "//li[text()='Priority set to ']/span"
    status_inside_editor = "div[data-test-id='add-update-ticket-action_change-status_trigger']>div[" \
                           "data-test-id='ticket-box_status']"
    priority_inside_editor = "span.hf-floating-editor_priority div.hf-ticket-action_label+div[" \
                             "data-test-id='ticket-box_priority']"
    tags_inside_editor = "div[data-test-id='editor-add-tags-trigger']>div"

