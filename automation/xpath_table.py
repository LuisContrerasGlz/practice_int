import time  # For sleep functions

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a WebDriver instance, pointing to the specific browser (e.g., Chrome)
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get('https://www.premierleague.com/tables')

    # Example of clicking a cookie consent button
    ele1 = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    ActionChains(driver).click(ele1).perform()
    time.sleep(2)  # Delay for actions to take effect
    
    # Click another button or link
    ele2 = driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/a[2]')
    ActionChains(driver).click(ele2).perform()
    time.sleep(2)  # Delay

    # Loop through a range of indices, similar to the original script
    for i in range(1, 40, 2):
        # Construct the XPath for the current index
        xpa = f'//*[@id="mainContent"]/div[3]/div[1]/div[5]/div/div/div/table/tbody/tr[{i}]/td[2]/a/span[2]'
        
        print(xpa)  # Print the current XPath
        
        # Find and click the element
        ele = driver.find_element(By.XPATH, xpa)
        ActionChains(driver).click(ele).perform()
        
        # Wait for the action to complete
        time.sleep(2)
        
        # Navigate back
        driver.back()

finally:
    # Close the browser window when done
    driver.quit()