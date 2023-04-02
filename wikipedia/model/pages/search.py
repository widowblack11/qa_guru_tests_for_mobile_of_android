import allure
from selene.support.shared import browser


def tap_on_search_field():
    with allure.step('Нажать на строку поиска'):
        browser.element('Search Wikipedia').tap()


def find_article(value):
    with allure.step('Найти статью'):
        browser.element('#search_src_text').type(value)


def open_article():
    with allure.step('Открыть статью'):
        browser.element('«Ancient Greek goddess of the Moon»').tap()


