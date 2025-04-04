from pages.modal_dialogs import ModalDialogsPage
import time  # Только для паузы перед проверкой


def test_modal_elements(browser):
    page = ModalDialogsPage(browser)
    page.visit()
    assert page.buttons.check_count_elements(2)



def test_navigation_modal(browser):
    page = ModalDialogsPage(browser)
    page.visit()
    browser.refresh()
    page.icon.click()
    browser.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    browser.forward()
    time.sleep(2)
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
