from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep, time

BASE_URL = 'https://www.target.com/'
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_INPUT_FIELD = (By.ID, 'search')
ADD_TO_CART = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
VIEW_CART_BTN = (By.XPATH, "//a[contains(text(), 'View cart')]")


@when('the user clicks the add to cart button')
def add_item_to_cart(context):
    sleep(9)
    context.driver.find_element(*ADD_TO_CART).click()


@when('confirm add to cart on side navigation')
def click_add_to_cart_on_side_nav(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART)
    ).click()


@when("the user clicks on the first search result")
def step_click_first_item(context):
    sleep(5)
    first_item = context.driver.find_element(By.CSS_SELECTOR, '[data-test="product-title"]')
    first_item.click()
    sleep(3)  # Wait for product page


@then('verify results for "{search_term}" should be displayed')
def verify_results(context, search_term):
    actual_text = context.driver.findElement(By.XPATH, "//div[@data-test='lp-resultsCount']").text()
    assert search_term in actual_text, 'error'


@when('click view cart')
def click_view_cart(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(VIEW_CART_BTN)
    ).click()
