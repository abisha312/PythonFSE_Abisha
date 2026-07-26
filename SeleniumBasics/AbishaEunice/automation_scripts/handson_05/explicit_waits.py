"""
Hands-On 5 - Task 2

Explicit Wait:
Waits for a specific condition before continuing.

Implicit Wait:
Applied globally for all elements.

Fluent Wait:
Allows custom polling frequency and ignored exceptions.

visibility_of_element_located:
Checks whether an element is visible.

element_to_be_clickable:
Checks whether element is visible, enabled, and clickable.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()


driver.get(
    "https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/"
)


wait = WebDriverWait(driver, 10)


# --------------------------------------
# Explicit Wait - Click Button
# --------------------------------------

button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(text(),'Normal Success Message')]"
        )
    )
)

button.click()

input("Check the alert and press Enter...")


# --------------------------------------
# Wait for Success Alert
# --------------------------------------

# Wait for alert visibility

# Wait for success alert

alert = wait.until(
    EC.visibility_of_element_located(
        (
            By.CSS_SELECTOR,
            "div.alert-success"
        )
    )
)

print("Alert Message:")
print(alert.text)


assert "successfully" in alert.text.lower()

print("Alert validation passed")


# --------------------------------------
# Compare sleep vs explicit wait
# --------------------------------------

driver.refresh()


start = time.time()

time.sleep(3)

end = time.time()

print(
    "time.sleep execution:",
    end - start
)


driver.refresh()


start = time.time()

wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(text(),'Click Me')]"
        )
    )
)

end = time.time()


print(
    "Explicit wait execution:",
    end - start
)


# --------------------------------------
# Fluent Wait Example
# --------------------------------------

driver.get(
    "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
)


fluent_wait = WebDriverWait(
    driver,
    10,
    poll_frequency=0.5,
    ignored_exceptions=[
        NoSuchElementException
    ]
)


row = fluent_wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//table/tbody/tr[1]"
        )
    )
)


print("Table Row Found:")
print(row.text)


driver.quit()