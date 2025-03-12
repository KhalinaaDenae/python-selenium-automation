import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



"""
Part 1 : 
Create a test case for the SignIn page
"""
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()



# Test case : Users can navigate to SignIn page
# open the url
driver.get('https://www.target.com/')


# Click SignIn button

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

# Wait for side navigation to appear
time.sleep(5)

# Click SignIn from side navigation

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# Wait for sign in page to load
time.sleep(5)


# Verify SignIn page opened:

# Sign into your Target account” text is shown,

signInText = driver.find_element(By.TAG_NAME, "span").text

print(signInText)

# SignIn button is shown

driver.find_element(By.ID, "login")


"""
Part 2: 
Practice with locators 
"""
# Amazon logo

# amazonLogo = driver.find_element(By.CLASS_NAME, "a-icon a-icon-logo")

# Email field

# emailField = driver.find_element(By.ID, 'ap_email').send_keys("testing")

# Continue button

# continueBtn = driver.find_element(By.ID, "continue")

# Conditions of use link

# conditionsLink = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")

# Privacy Notice link

#privacyLink = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")

# Need help link

#helpLink = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link

#forgotPassword =  driver.find_element(By.ID, "auth-fpp-link-bottom")


# Other issues with Sign-In link

#otherIssues =  driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button

#createAccount = driver.find_element(By.ID, "createAccountSubmit")




