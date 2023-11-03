from selenium import webdriver # pip install selenium

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open the main URL
driver.get('https://www.example.com')

# Store the main window handle
main_window_handle = driver.current_window_handle

# Open a new window by clicking a link (simulated here)
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Get all window handles
all_handles = driver.window_handles

# Loop through the handles to switch to the new window
for handle in all_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        # Perform actions on the new window
        print(f"Current URL in new window: {driver.current_url}")
        driver.get("https://www.bing.com")  # Navigating to Bing in the new window
        # Close the new window/tab
        driver.close()
        break

# Switch back to the main window
driver.switch_to.window(main_window_handle)
print(f"Current URL in main window: {driver.current_url}")

# Close the main window
driver.quit()
