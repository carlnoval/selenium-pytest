"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

# manually entered from course
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

  # locators as tuple class variables since only one immutable varaibale is needed
  SEARCH_INPUT = (By.ID, "search_form_input_homepage")

  # dunder init method constructor
  def __init__(self, browser):
    self.browser = browser

  def load(self):
    # TODO
    pass

  def search(self, phrase):
    # TODO
    pass
