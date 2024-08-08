from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

# Set up the Edge WebDriver with the downloaded WebDriver path
service = Service(executable_path='C:/Users/Alfaize/Desktop/New folder/msedgedriver.exe')
options = webdriver.EdgeOptions()
options.use_chromium = True
driver = webdriver.Edge(service=service, options=options)

try:
    # Open the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Locate the username field and enter the username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Locate the password field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Locate the login button and click it
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Verify the login by checking for a specific element on the landing page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.flash.success"))
    )
    print("Login successful!")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
