"""

StaleElementReferenceException is a common exception encountered in Selenium WebDriver 
when an element that was previously found on a web page becomes stale or no longer exists in the current state of the Document Object Model (DOM). 
This exception occurs when the state of an element changes, usually due to a page refresh, navigation, or modification, 
making the previously located element reference no longer valid.


"""

"""

When an element becomes stale, you need to re-locate or re-find the element on the page to interact with it again. 
To prevent this exception, you can re-locate the element before interacting with it or catch and handle the exception by re-finding the element to ensure it's current before performing any actions.

"""

# pip install selenium

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

# Assuming driver is an instantiated WebDriver (e.g., Chrome or Firefox)

# Initial attempt to find the element
try:
    element = driver.find_element(By.ID, "elementId")
    # Perform some action that might cause the element to become stale
    # For example, a page refresh or an AJAX update
    
    # If an action causes the element to become stale, a StaleElementReferenceException might occur
    # To handle this exception, re-locate the element before interacting with it again
    element = driver.find_element(By.ID, "elementId")  # Re-find the element
    
    # Perform the intended action with the re-found element
    element.click()  # For example, clicking the element
except StaleElementReferenceException as e:
    print("Stale Element Exception occurred. Re-locating the element.")
    element = driver.find_element(By.ID, "elementId")  # Re-find the element after exception
    element.click()  # Perform the action after re-finding the element


"""

Java:

WebElement element = driver.findElement(By.id("elementId"));
// Perform an action that causes the page to refresh or modify the element
// Now, re-find the element before interacting with it
element = driver.findElement(By.id("elementId"));
element.click(); // Perform the intended action with the re-found element


"""