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

        # Verify the presence of the first XPath
        xpath_to_verify = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/div"
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_to_verify))
            )
            print(f"XPath {xpath_to_verify} verified. URL reached.")
        except Exception as e:
            print(f"XPath {xpath_to_verify} not found. URL didn't reach as expected.")
            return  # Exit the script if the first XPath is not verified

        # Verify the presence of the second XPath and enter the user ID
        user_id_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[1]/div[2]/input"
        try:
            user_id_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, user_id_xpath))
            )
            # Enter the user ID
            user_id_input.send_keys("karthikeyan")
            print("User ID entered.")
        except Exception as e:
            print("Unable to enter User ID.")

        # Verify the presence of the third XPath and enter the password
        password_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[2]/div[2]/input"
        try:
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, password_xpath))
            )
            # Enter the password
            password_input.send_keys("karthi123")
            print("Password entered.")
        except Exception as e:
            print("Unable to enter Password.")

        # Click the log-on button
        logon_button_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[3]/a[1]"
        try:
            logon_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, logon_button_xpath))
            )
            logon_button.click()
            print("Log On clicked.")
        except Exception as e:
            print("Log On not clicked.")

        # Add additional interactions with the web page here if needed

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
