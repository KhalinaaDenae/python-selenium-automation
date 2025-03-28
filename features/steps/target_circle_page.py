from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then

BASE_URL = 'https://www.target.com/circle'
BENEFIT_CELLS = (By.CSS_SELECTOR, ".cell-item-content")


@given('user is on the Target Circle homepage')
def open_target_circle_main(context):
    context.driver.get(BASE_URL)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(BENEFIT_CELLS)
    )  # Wait until at least one benefit cell appears


@then('verify at least 10 benefit cells shown')
def verify_benefit_cells(context):
    benefits = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(BENEFIT_CELLS)
    )
    assert len(benefits) >= 10, f"Expected at least 10 benefit cells, but found {len(benefits)}"
