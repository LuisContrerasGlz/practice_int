import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Create a WebDriver instance for Chrome
driver = webdriver.Chrome()

try:
    # Explicit wait configuration
    wait = WebDriverWait(driver, 15)  # Timeout of 15 seconds

    # Navigate to the website
    driver.get('https://www.premierleague.com/tables')

    time.sleep(3) 
    # Wait for an element to be visible
    ele_visible = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
    ele_visible.click()  # Click the element after confirming it is visible

    time.sleep(3) 
    # Wait for another element to be present (not necessarily clickable)
    ele_present = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/nav/a[2]')))
    ele_present.click()  # Click the element once it's present in the DOM

    time.sleep(3) 
    # Example of waiting for visible elements in a loop
    for i in range(1, 40, 2):
        # Construct the XPath for the current index
        xpa = f'//*[@id="mainContent"]/div[3]/div[1]/div[5]/div/div/div/table/tbody/tr[{i}]/td[2]/a/span[2]'
        
        print(xpa)  # For debugging
        
        # Wait until the element is visible
        ele_visible_in_loop = wait.until(EC.visibility_of_element_located((By.XPATH, xpa)))
        
        # Get the text from the element
        texto_elemento = ele_visible_in_loop.text
        print(texto_elemento)

        # Click the visible element
        ele_visible_in_loop.click()
        
        # Navigate back and ensure the original page is ready
        driver.back()
        
        # Wait until the same element is visible again
        wait.until(EC.visibility_of_element_located((By.XPATH, xpa)))

except TimeoutException:
    print("Timeout occurred. Consider increasing the timeout duration or verifying your XPath.")

finally:
    # Proper cleanup to close the WebDriver
    driver.quit()
