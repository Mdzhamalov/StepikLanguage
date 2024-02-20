from selenium.webdriver.common.by import By


def test_is_button_add_to_basket_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_basket = len(browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']"))
    assert add_to_basket > 0, "Can't find button 'Add to basket'"
