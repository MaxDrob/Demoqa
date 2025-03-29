from selenium.common.exceptions import NoSuchFrameException

from components.components import WebElement
from pages.base_page import BasePage

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.center_text = WebElement(driver, '.col-md-6')
