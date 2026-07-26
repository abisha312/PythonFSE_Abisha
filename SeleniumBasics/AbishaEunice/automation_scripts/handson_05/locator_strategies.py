"""
Hands-On 5 - Task 1

Locator Strategy Ranking (Best to Worst):

1. ID
- Most preferred because IDs are unique, fast, and readable.

2. Name
- Good if the name attribute is stable and unique.

3. CSS Selector
- Fast and readable. Works well for most cases.

4. Class Name
- Useful but can become unreliable if classes change frequently.

5. Relative XPath
- Flexible and useful when CSS cannot locate elements.

6. Absolute XPath
- Least preferred because any HTML structure change breaks it.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get(
    "https://www.lambdatest.com/selenium-playground/simple-form-demo"
)

driver.implicitly_wait(10)


# Target element:
# Message input field

# 1. ID Locator
message_id = driver.find_element(
    By.ID,
    "user-message"
)

print("ID locator passed")


# 2. NAME Locator
message_name = driver.find_element(
    By.NAME,
    "message"
)

print("NAME locator passed")


# 3. CLASS NAME Locator
message_class = driver.find_element(
    By.CLASS_NAME,
    "form-control"
)

print("CLASS NAME locator passed")


# 4. TAG NAME Locator
message_tag = driver.find_element(
    By.TAG_NAME,
    "input"
)

print("TAG NAME locator passed")


# 5. Absolute XPath
# Copy this XPath from Chrome DevTools:
# Right click element -> Copy -> Copy XPath

message_absolute_xpath = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/main/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input"
)

print("Absolute XPath locator passed")


# 6. Relative XPath
message_relative_xpath = driver.find_element(
    By.XPATH,
    '//*[@id="user-message"]'
)

print("Relative XPath locator passed")


# CSS Selector 1 - ID
css_id = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

print("CSS ID passed")


# CSS Selector using attribute

css_attribute = driver.find_element(
    By.CSS_SELECTOR,
    "input[id='user-message']"
)

print("CSS Attribute passed")


# CSS Selector 3 - Parent child
css_parent = driver.find_element(
    By.CSS_SELECTOR,
    "div input#user-message"
)

print("CSS Parent Child passed")


# Checkbox Demo

driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)


# XPath text()
option1 = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("XPath text() passed")


# XPath contains()
options = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print(
    "Total options found:",
    len(options)
)


input("Press Enter to close...")
driver.quit()