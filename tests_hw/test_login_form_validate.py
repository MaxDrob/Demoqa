from components.components import WebElement


def test_login_form_validation(browser):

    browser.get('https://demoqa.com/automation-practice-form')


    first_name = WebElement(browser, '#firstName')
    last_name = WebElement(browser, '#lastName')
    email = WebElement(browser, '#userEmail')
    submit = WebElement(browser, '#submit')
    form = WebElement(browser, '#userForm')


    assert first_name.get_dom_attribute('placeholder') == 'First Name'
    assert last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert email.get_dom_attribute('placeholder') == 'name@example.com'
    assert email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'


    submit.click_force()
    assert 'was-validated' in form.get_dom_attribute('class')