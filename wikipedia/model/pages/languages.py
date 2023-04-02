import allure
from selene import be
from selene.support.shared import browser


def open_language_page():
    with allure.step('Открыть страницу смены языка'):
        browser.element('#page_language').tap()


def tap_on_search_field():
    with allure.step('Нажать на поле поиска языка'):
        browser.element('#menu_search_language').tap()


def find_language(value):
    with allure.step('Найти язык'):
        browser.element('#search_src_text').type(value)


def assert_language_was_found():
    with allure.step('Язык был найден'):
        browser.element('«Russian»').should(be.visible)

