from selenium.webdriver.common.by import By
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
    sleep(2)  # Wait for the page to load


@given('the user clicks on the "sign in" button')
def click_sign_in(context):
    # Click SignIn button
    context.driver.find_element(SIGN_IN_BTN).click()


@given('the side navigation menu opens')
def side_nav_opens(context):
    # Wait for side navigation to appear
    sleep(5)


@given('the user is on the Target homepage with an empty cart')
def target_homepage_open(context):
    context.driver.get(BASE_URL)
    sleep(5)  # Wait for the page to load

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
    context.driver.find_element(CART_ICON)
    context.driver.find_element(CART_ICON).click()
    sleep(2)



@when('the user clicks on the "sign on" button on the side navigation')
def click_sign_in_on_side_nav(context):
    context.driver.find_element(SIDE_NAV_SIGN_IN_BTN).click()
    sleep(5)

