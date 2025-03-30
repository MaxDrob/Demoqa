from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    text_page = DemoQa(browser)
    text_page .visit()

    footer_text = text_page.footer.get_text()
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_center_text_on_elements_page(browser):
    text_page = DemoQa(browser)
    text_page.visit()

    text_page.btn_elements.click()
    elements_page = ElementsPage(browser)

    center_text = elements_page.center_text.get_text()
    assert center_text == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()