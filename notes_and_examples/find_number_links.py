from selenium import webdriver # pip install selenium

# Instantiate the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get('https://www.google.com')

# Find all the anchor elements (links)
links_found = driver.find_elements_by_tag_name('a')

# Get the count of the links
num_of_links = len(links_found)
print("Number of links on Google homepage:", num_of_links)

# Close the browser
driver.quit()

"""

This code navigates to the Google homepage, finds all the anchor elements (links) using driver.find_elements_by_tag_name('a'), 
counts the number of links, and prints the total number of links found on the Google homepage.

"""
