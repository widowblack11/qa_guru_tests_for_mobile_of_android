import allure
from allure_commons.types import Severity

from wikipedia.model import app
from wikipedia.model.pages import search, languages


@allure.title('Смена языка')
@allure.tag('mobile')
@allure.label('owner', 'o_prokopenko')
@allure.severity(Severity.CRITICAL)
@allure.feature('Языки')
@allure.story('Wikipedia')
def test_find_language():
    app.given_opened()

    search.tap_on_search_field()
    search.find_article('Selene')
    search.open_article()
    languages.open_language_page()
    languages.tap_on_search_field()
    languages.find_language('russian')

    languages.assert_language_was_found()