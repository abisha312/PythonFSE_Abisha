"""
Hands-On 4
Task 1

Selenium Architecture

1. WebDriver
- WebDriver is the main component of Selenium.
- It communicates directly with the browser using browser-specific drivers.
- It allows automation scripts to perform browser actions such as clicking, typing, and navigation.

2. Selenium Grid
- Selenium Grid allows execution of tests on multiple machines and browsers simultaneously.
- It helps perform parallel execution and cross-browser testing.

3. Selenium IDE
- Selenium IDE is a browser extension.
- It is mainly used for recording and playing back automation scripts.
- It can also generate automation code in multiple programming languages.

Implicit Wait Note:
Implicit wait is applied globally to all element searches.
Using implicit waits is generally considered a bad practice because it can slow down tests and is less flexible.
Explicit waits wait only for specific conditions, making tests faster and more reliable.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome options
options = webdriver.ChromeOptions()

# Headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Global implicit wait
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:")
print(driver.title)

driver.quit()