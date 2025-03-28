from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = 'https://www.target.com/p/A-91511634'
COLOR_OPTIONS = (By.XPATH, "//*[contains(@class, 'VariationComponent')]")
SELECTED_COLOR = (By.XPATH, "//*[contains(@class, 'VariationComponent') and @aria-checked='true']")



@given('Open target product page')
def open_product_page(context):
    context.driver.get(BASE_URL)
    time.sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    @then('Verify user can click through colors')
    def click_and_verify_colors(context):
        expected_colors = ['white/sand/tan', 'dark khaki', 'grey', 'navy/tan', 'white/navy/red']
        actual_colors = []

        colors = context.driver.find_elements(*COLOR_OPTIONS)

        for color in colors:
            # Click on the color
            color.click()
            time.sleep(2)  # Allow the UI to update after click

            # Capture the selected color element
            try:
                selected_color_element = WebDriverWait(context.driver, 5).until(
                    EC.presence_of_element_located(SELECTED_COLOR)
                )

                selected_color = selected_color_element.text
                actual_colors.append(selected_color)
                print(f"Selected color: {selected_color}")

            except Exception as e:
                print(f"Error: {str(e)}")

        # Verify that all expected colors are clicked
        for expected_color in expected_colors:
            assert expected_color in actual_colors, f"{expected_color} was not selected. Actual colors: {actual_colors}"