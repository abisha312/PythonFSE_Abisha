from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .base_page import BasePage


class DropdownPage(BasePage):

    DROPDOWN = (
        By.ID,
        "select-demo"
    )


    def select_day(self, day_name):

        dropdown = Select(
            self.driver.find_element(
                *self.DROPDOWN
            )
        )

        dropdown.select_by_visible_text(
            day_name
        )