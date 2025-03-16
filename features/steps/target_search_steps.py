from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target  main page')
def open_Target_main(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Search for tea')
def search_for_item(context):
    context.drive.find_element(By.ID, 'search').send_keys('tea')
    sleep(6)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
