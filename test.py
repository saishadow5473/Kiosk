from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Set up the Selenium WebDriver with options
    options = webdriver.ChromeOptions()
    # Comment the next line if you want to see the browser window
    options.add_argument('--headless')  # Use this if you're running headless
    # Actual path to Chrome binary (change this to the path on your machine)
    options.binary_location = '/usr/bin/google-chrome'

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Open the specified URL
        driver.get("https://kioskportal.indiahealthlink.com/portalm/Account/Login")

        # Add additional interactions with the web page here if needed

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
