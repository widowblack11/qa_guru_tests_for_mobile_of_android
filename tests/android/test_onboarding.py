
import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


text_title = (AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")
btn_continue = (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
main_page = (AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')


@allure.title('Просмотр экранов онбординга')
@allure.tag('mobile')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Онбординг')
@allure.story('Wikipedia')
def test_onboarding_screen():
    with allure.step('Check first screen'):
        browser.element(text_title).should(have.text("The Free Encyclopedia"))
        browser.element(btn_continue).click()
    with allure.step('Check second screen'):
        browser.element(text_title).should(have.text("New ways to explore"))
        browser.element(btn_continue).click()
    with allure.step('Check third screen'):
        browser.element(text_title).should(have.exact_text("Reading lists with sync"))
        browser.element(btn_continue).click()
    with allure.step('Check fourth screen'):
        browser.element(text_title).should(have.text("Send anonymous data"))


@allure.title('Пропуск онбординга')
@allure.tag('mobile')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Онбординг')
@allure.story('Wikipedia')
def test_open_app_without_onbording(skip_onboarding):
    with allure.step('Проверить,что появилась главная страница приложения,после пропуска онбординга'):
        browser.element(main_page).should(have.text('Customize your Explore feed'))

