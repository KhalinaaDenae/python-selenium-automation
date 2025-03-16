from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, time


@given('the user is logged out')
def open_target(context):
    context.driver.get("https://www.target.com/")
    sleep(2)  # Wait for the page to load


@given('the user clicks on the "sign in" button')
def click_sign_in(context):
    # Click SignIn button
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

@given('the side navigation menu opens')
def side_nav_opens(context):
    # Wait for side navigation to appear
    sleep(5)

@when('the user clicks on the "sign on" button on the side navigation')
def click_sign_in_on_side_nav(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('the sign in form should be displayed for the user')
def verify_sign_in_form(context):
    expected = "Sign into your Target account"
    actual = context.driver.find_element(By.TAG_NAME, "span").text
    assert expected == actual, f"Expected '{expected}', but got '{actual}'"
    print("Test Passed: Sign in form is displayed with the correct text.")



