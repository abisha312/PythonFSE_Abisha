from selenium.webdriver.common.by import By

from .base_page import BasePage


class SimpleFormPage(BasePage):

    MESSAGE_INPUT = (
        By.ID,
        "user-message"
    )

    SUBMIT_BUTTON = (
        By.ID,
        "showInput"
    )

    DISPLAY_MESSAGE = (
        By.ID,
        "message"
    )


    def enter_message(self, text):

        element = self.wait_for_element(
            self.MESSAGE_INPUT
        )

        element.send_keys(text)


    def click_submit(self):

        self.driver.find_element(
            *self.SUBMIT_BUTTON
        ).click()


    def get_displayed_message(self):

        element = self.wait_for_element(
            self.DISPLAY_MESSAGE
        )

        return element.text