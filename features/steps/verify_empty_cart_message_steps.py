from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('the user is on the Target homepage with an empty cart')
def target_homepage_open(context):
    context.driver.get("https://www.target.com/")
    sleep(2)  # Wait for the page to load


@when('the user clicks on the Cart icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.XPATH, '//a[contains(@href, "/cart")]')
    cart_icon.click()
    sleep(2)


@then('the message "Your cart is empty" should be displayed')
def check_message(context):
    message = context.driver.find_element(By.XPATH, '//span[contains(text(), "Your cart is empty")]')
    assert message.is_displayed(), "Empty cart message not found!"


