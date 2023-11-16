from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
            return  # Exit the script if Log On button is not clicked

        # Wait for 5 seconds
        time.sleep(5)

        # Verify the presence of the fourth XPath
        login_status_xpath = "/html/body/div/div[4]/div[2]/div[1]/a"
        try:
            login_status = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, login_status_xpath))
            )
            print("Login successful.")
        except Exception as e:
            print("Login unsuccessful.")

        # Click on the administration tab
        administration_tab_xpath = "/html/body/div/div[3]/ul/li[3]/a"
        try:
            administration_tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, administration_tab_xpath))
            )
            administration_tab.click()
            print("Clicked on Administration.")
        except Exception as e:
            print("Not clicked on Administration.")
            return  # Exit the script if Administration tab is not clicked

        # Click on the platform button
        platform_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/a[3]"
        try:
            platform_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, platform_button_xpath))
            )
            platform_button.click()
            print("Clicked on Platform.")
        except Exception as e:
            print("Not clicked on Platform.")
            return  # Exit the script if Platform button is not clicked

        # Click on the New button
        new_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div/a"
        try:
            new_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, new_button_xpath))
            )
            new_button.click()
            print("Clicked on New.")
        except Exception as e:
            print("Not clicked on New.")
            return  # Exit the script if New button is not clicked

        # Click on the Choose File button
        choose_file_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[2]/div/div/div/form/div/div[3]/div[2]/input"
        try:
            choose_file_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, choose_file_button_xpath))
            )
            choose_file_button.click()
            print("Clicked on Choose File.")
        except Exception as e:
            print("Not clicked on Choose File.")
            return  # Exit the script if Choose File button is not clicked

        # Provide the local file path to the file input field
        local_file_path = r"E:\ubuntu folder\3.13.2-E-Sanjeevani.zip"
        try:
            choose_file_button.send_keys(local_file_path)
            print(f"Selected the file: {local_file_path}")
        except Exception as e:
            print("Unable to select the file.")

        # Add additional interactions with the web page here if needed

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
