from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/modal-dialogs")
        self.icon = WebElement(driver, '#app > header > a')
        self.buttons = WebElement(driver, 'button.btn-primary:not(.navbar-toggler)')
