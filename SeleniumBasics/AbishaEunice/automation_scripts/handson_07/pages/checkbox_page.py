from selenium.webdriver.common.by import By

from .base_page import BasePage


class CheckboxPage(BasePage):

    CHECKBOXES = (
        By.XPATH,
        "//input[@type='checkbox']"
    )


    def check_option(self, index):

        boxes = self.driver.find_elements(
            *self.CHECKBOXES
        )

        if not boxes[index].is_selected():
            boxes[index].click()



    def uncheck_option(self, index):

        boxes = self.driver.find_elements(
            *self.CHECKBOXES
        )

        if boxes[index].is_selected():
            boxes[index].click()



    def is_option_checked(self,index):

        boxes = self.driver.find_elements(
            *self.CHECKBOXES
        )

        return boxes[index].is_selected()