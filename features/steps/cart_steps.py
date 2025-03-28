from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('the message "Your cart is empty" should be displayed')
def check_message(context):
    message = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Your cart is empty")]'))
    )
    assert message.is_displayed(), "Empty cart message not found!"
@then('verify cart has 1 item')
def check_item_count(context):
    cart_summary = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(CART_SUMMARY)
    )
    cart_summary_text = cart_summary.text
    assert "1 item" in cart_summary_text, f"Expected '1 item', but got: {cart_summary_text}"