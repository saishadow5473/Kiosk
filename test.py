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
        driver.get("https://kioskportal.indiahealthlink.com/portalm")

        # Check if the URL was successfully reached
        if "Login" in driver.title:
            print("URL successfully reached")

            # Verify the presence of the element with the given XPath
            xpath_to_verify = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[3]/a[1]"
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_to_verify))
                )
                print(f"XPath {xpath_to_verify} verified. URL reached.")
            except Exception as e:
                print(f"XPath {xpath_to_verify} not found. URL didn't reach as expected.")

        else:
            print("URL didn't reach as expected")

        # Add additional interactions with the web page here if needed

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
