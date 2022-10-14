"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

# dependencies
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.XPATH, "//a[@data-testid='result-title-a']")
    SEARCH_INPUT = (By.ID, "search_form_input")

    # dunder init method constructor
    def __init__(self, browser):
        self.browser = browser

    # returns a list/array of all link titles
    def result_link_titles(self):
        links_titles = self.browser.find_elements(*self.RESULT_LINKS)
        # returns array of strings from link titles
        titles = [link.text for link in links_titles]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # for input elements .text() is always going to give an empty string
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title
