
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser

text_title = (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
btn_continue = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")


def test_onboarding_screen():
    with allure.step('Проверка стартового экрана'):
        browser.element(text_title).should(have.text("The Free Encyclopedia"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к второму экрана'):
        browser.element(text_title).should(have.text("New ways to explore"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к третьему экрану'):
        browser.element(text_title).should(have.exact_text("Reading lists with sync"))
        browser.element(btn_continue).click()
    with allure.step('Проверка перехода к четвертому экрана'):
        browser.element(text_title).should(have.text("Send anonymous data"))
