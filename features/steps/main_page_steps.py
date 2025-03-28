from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

BASE_URL = 'https://www.target.com/'
SIGN_IN_BTN = (By.XPATH, "//span[text()='Sign in']")
SIDE_NAV_SIGN_IN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
CART_ICON = (By.XPATH, '//a[contains(@href, "/cart")]')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_INPUT_FIELD = (By.ID, "searchMobile")


@given('the user is logged out')
def open_target(context):
    context.driver.get(BASE_URL)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(SIGN_IN_BTN)
    )  # Wait for the sign-in button to appear


@given('the user clicks on the "sign in" button')
def click_sign_in(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(SIGN_IN_BTN)
    ).click()


@given('the side navigation menu opens')
def side_nav_opens(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(SIDE_NAV_SIGN_IN_BTN)
    )  # Wait for the side navigation menu to appear


@given('the user is on the Target homepage with an empty cart')
def target_homepage_open(context):
    context.driver.get(BASE_URL)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(SIGN_IN_BTN)
    )  # Ensure the homepage loads


@when('the user searches for "{search_term}"')
def step_search_for_item(context, search_term):
    search_box = context.driver.find_element(By.NAME, "searchTerm")
    search_box.send_keys(search_term)
    sleep(4)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)
    # Wait for results to load


@when('the user clicks on the Cart icon')
def click_cart_icon(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(CART_ICON)
    ).click()


@when('the user clicks on the "sign on" button on the side navigation')
def click_sign_in_on_side_nav(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(SIDE_NAV_SIGN_IN_BTN)
    ).click()
