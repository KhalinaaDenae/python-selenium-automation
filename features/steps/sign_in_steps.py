from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, time


@then('the sign in form should be displayed for the user')
def verify_sign_in_form(context):
    expected = "Sign into your Target account"
    actual = context.driver.find_element(By.TAG_NAME, "span").text
    assert expected == actual, f"Expected '{expected}', but got '{actual}'"
    print("Test Passed: Sign in form is displayed with the correct text.")


