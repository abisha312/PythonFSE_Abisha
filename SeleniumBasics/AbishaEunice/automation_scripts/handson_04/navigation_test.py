"""
Hands-On 4
Task 2

This script demonstrates:

- Navigation
- URL Assertion
- Opening New Tabs
- Window Switching
- Screenshot Capture
- Window Resize

Maintaining a consistent browser window size is important because
responsive web pages change their layout depending on screen resolution.
Using a fixed size ensures consistent automation results.
"""

import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.implicitly_wait(10)

# Click Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("URL Assertion Passed")

# Navigate back
driver.back()

# Open Google in new tab
driver.execute_script("window.open('https://www.google.com');")

# Display window handles
print("Window Handles:")
print(driver.window_handles)

# Switch to Google
driver.switch_to.window(driver.window_handles[1])

print("Google Page Title:")
print(driver.title)

# Switch back
driver.switch_to.window(driver.window_handles[0])

# Screenshot
driver.save_screenshot("playground_screenshot.png")

if os.path.exists("playground_screenshot.png"):
    print("Screenshot saved successfully")

# Window size
print("Current Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("Updated Window Size:")
print(driver.get_window_size())

driver.quit()