import time
from components.components import WebElement


def test_text_box(browser):
    browser.get('https://demoqa.com/text-box')

    name_field = WebElement(browser, '#userName')
    address_field = WebElement(browser, '#currentAddress')
    submit_btn = WebElement(browser, '#submit')
    output_name = WebElement(browser, '#name')
    output_address = WebElement(browser, '#output #currentAddress')

    test_name = "Tester one"
    test_address = "Tester's street, 90210"

    name_field.send_keys(test_name)
    address_field.send_keys(test_address)

    submit_btn.click_force()
    time.sleep(5)

    assert test_name in output_name.get_text()
    assert test_address in output_address.get_text()