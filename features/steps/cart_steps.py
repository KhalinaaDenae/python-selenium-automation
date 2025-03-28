from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]")


@then('the message "Your cart is empty" should be displayed')
def check_message(context):
    message = context.driver.find_element(By.XPATH, '//span[contains(text(), "Your cart is empty")]')
    assert message.is_displayed(), "Empty cart message not found!"


@then('verify cart has 1 item')
def check_item_count(context):
    sleep(5)
    cart_summary_text = context.driver.find_element(*CART_SUMMARY).text
    assert "1 item" in cart_summary_text, f"Expected '1 item', but got: {cart_summary_text}"
