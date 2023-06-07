from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope='session', autouse=True)
def before_all():
    browser.config.window_height = 600
    browser.config.window_width = 800


@pytest.fixture()
def before_each():
    browser.open('https://google.com')


def test_search_results_found(before_each):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_results_not_found(before_each):
    no_result_text = 'thisIsTheRandomStringThatShouldNotBeFoundInGooGle'
    browser.element('[name="q"]').should(be.blank).type(no_result_text).press_enter()
    browser.element('[id="res"]').should(have.text('Your search - ' + no_result_text + ' - did not match any documents.'))
