import asyncio
from pyppeteer import launch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

async def file_upload_pyppeteer():
    # Launch headless browser
    browser = await launch({'headless': True, 'args': ['--no-sandbox', '--disable-dev-shm-usage']})
    page = await browser.newPage()

    try:
        # Open the specified URL
        await page.goto("https://kioskportal.indiahealthlink.com/portalm/Account/Login", waitUntil='domcontentloaded')

        # Verify the presence of the first XPath
        xpath_to_verify = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/div"
        try:
            await page.waitForXPath(xpath_to_verify)
            print(f"XPath {xpath_to_verify} verified. URL reached.")
        except Exception as e:
            print(f"XPath {xpath_to_verify} not found. URL didn't reach as expected.")
            return  # Exit the script if the first XPath is not verified

        # Verify the presence of the second XPath and enter the user ID
        user_id_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[1]/div[2]/input"
        try:
            user_id_input = await page.waitForXPath(user_id_xpath)
            # Enter the user ID
            await user_id_input.type("karthikeyan")
            print("User ID entered.")
        except Exception as e:
            print("Unable to enter User ID.")
            time.sleep(10)

        # Verify the presence of the third XPath and enter the password
        password_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[2]/div[2]/input"
        try:
            password_input = await page.waitForXPath(password_xpath)
            # Enter the password
            await password_input.type("karthi123")
            print("Password entered.")
        except Exception as e:
            print("Unable to enter Password.")
            time.sleep(10)

        # Click the log-on button
        logon_button_xpath = "/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/form/div/div[3]/a[1]"
        try:
            logon_button = await page.waitForXPath(logon_button_xpath)
            await logon_button.click()
            print("Log On clicked.")
        except Exception as e:
            print("Log On not clicked.")
            return  # Exit the script if Log On button is not clicked

        # Wait for 5 seconds
        await page.waitForTimeout(5000)

        # Verify the presence of the fourth XPath
        login_status_xpath = "/html/body/div/div[4]/div[2]/div[1]/a"
        try:
            await page.waitForXPath(login_status_xpath)
            print("Login successful.")
        except Exception as e:
            print("Login unsuccessful.")
            await page.waitForTimeout(5000)

        # Click on the administration tab
        administration_tab_xpath = "/html/body/div/div[3]/ul/li[3]/a"
        try:
            administration_tab = await page.waitForXPath(administration_tab_xpath)
            await administration_tab.click()
            print("Clicked on Administration.")
        except Exception as e:
            print("Not clicked on Administration.")
            return  # Exit the script if Administration tab is not clicked
        await page.waitForTimeout(5000)

        # Click on the platform button
        platform_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/a[3]"
        try:
            platform_button = await page.waitForXPath(platform_button_xpath)
            await platform_button.click()
            print("Clicked on Platform.")
        except Exception as e:
            print("Not clicked on Platform.")
            return  # Exit the script if Platform button is not clicked
        await page.waitForTimeout(5000)

        # Click on the New button
        new_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[1]/div/div/a"
        try:
            new_button = await page.waitForXPath(new_button_xpath)
            await new_button.click()
            print("Clicked on New.")
        except Exception as e:
            print("Not clicked on New.")
            return  # Exit the script if New button is not clicked
        await page.waitForTimeout(5000)

        # Click on the Choose File button
        choose_file_button_xpath = "/html/body/div/div[4]/div[2]/div[3]/div[2]/div/div/div/form/div/div[3]/div[2]"
        try:
            choose_file_input = await page.waitForXPath(choose_file_button_xpath)
            await choose_file_input.click()
            print("Clicked on Choose File.")
        except Exception as e:
            print("Not clicked on Choose File.")
            return  # Exit the script if Choose File button is not clicked
        await page.waitForTimeout(5000)

        # Specify the file name to be uploaded (without the path)
        file_name = "README.md"

        # Set the file path in the file input field using pyppeteer
        try:
            await page.setInputFiles('input[type="file"]', file_name)
            print("File uploaded.")
        except Exception as e:
            print("Unable to upload file.")
            return  # Exit the script if file upload is unsuccessful

        # Continue with the rest of your Selenium script
        # Set up the Selenium WebDriver with options
        options = webdriver.ChromeOptions()
        # Comment the next line if you want to see the browser window
        options.add_argument('--headless')  # Use this if you're running headless
        # Actual path to Chrome binary (change this to the path on your machine)
        options.binary_location = '/usr/bin/google-chrome'
        # options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome(options=options)

        try:
            # Open the specified URL
            driver.get("https://kioskportal.indiahealthlink.com/portalm/Account/Login")
            time.sleep(10)

            # ... (continue with the rest of your Selenium script)
            # For example, you can use WebDriverWait and other Selenium commands here

        finally:
            # Close the browser window
            driver.quit()

    finally:
        # Close the browser
        await browser.close()

# Run the event loop for pyppeteer
asyncio.get_event_loop().run_until_complete(file_upload_pyppeteer())
