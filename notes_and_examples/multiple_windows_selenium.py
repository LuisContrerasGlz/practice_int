from selenium import webdriver # pip install selenium
import time

# Initialize the WebDriver (ensure the ChromeDriver path is set correctly)
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Navigate to Google
driver.get("https://www.google.com")

# Store the parent window handle
parent_window = driver.current_window_handle

# Clicking "News" to open a new window
news_link = driver.find_element_by_link_text("News")
news_link.click()

# Wait for the new window to open (wait time can be adjusted as needed)
time.sleep(2)

# Get all window handles after the new window has opened
all_handles = driver.window_handles

# Loop through the window handles
for handle in all_handles:
    if handle != parent_window:
        # Switch to the new window
        driver.switch_to.window(handle)
        # Perform actions in the new window
        print("Switched to the new window")
        # Get the title of the new window
        print("New Window Title:", driver.title)
        # Get the URL of the new window
        print("New Window URL:", driver.current_url)
        # Wait for demonstration purposes
        time.sleep(2)
        # Close the new window
        driver.close()

# Switch back to the original window
driver.switch_to.window(parent_window)
# Perform actions in the original window
print("Switched back to the parent window")
# For example, get the title of the parent window
print("Parent Window Title:", driver.title)

# Close the browser
driver.quit()
