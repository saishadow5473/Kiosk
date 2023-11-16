from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Set up the web driver (make sure you have the appropriate webdriver installed, e.g., ChromeDriver)
driver = webdriver.Chrome()

# Open the URL
url = "https://kioskportal.indiahealthlink.com/portalm"
driver.get(url)

try:
    # Find the element using XPath
    element = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[3]/div[2]/div/div/div/div")
    
    # If the element is found, print "URL reached"
    print("URL reached")

except NoSuchElementException:
    # If the element is not found, print "URL not reached"
    print("URL not reached")

finally:
    # Close the browser window
    driver.quit()
