from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    x_element = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    x = x_element
    assert x, f"Button was not found"