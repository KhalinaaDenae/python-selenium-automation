from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep, time

BASE_URL = 'https://www.target.com/circle'
benefit_cells = (By.CSS_SELECTOR,  "div[class*='styles__BenefitCard']")


@given('user is on the Target Circle homepage')
def open_target_circle_main(context):
    context.driver.get(BASE_URL)
    sleep(3)


@then('verify at least 10 benefit cells shown')
def verify_benefit_cells(context):
    time.sleep(5)
    assert len(benefit_cells) >= 10, f"Expected at least 10 benefit cells, but found {len(benefit_cells)}"

