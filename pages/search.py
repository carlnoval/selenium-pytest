"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

# dependencies
# from typing import KeysView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:

  URL = 'htts://www.duckduckgo.com'

  # search input locator as tuple class variables since only one immutable varaibale is needed
  SEARCH_INPUT = (By.ID, "search_form_input_homepage")

  # dunder init method constructor
  def __init__(self, browser):
    self.browser = browser

  # loads a web page in the current browser session
  def load(self):
    self.browser.get(self.URL)

  # 
  def search(self, phrase):
    # webdriver locates the element using the class variable tuple
    # find_element takes in two arguments(By tag/attribute and value)
    search_intput = self.browser.find_element(*self.SEARCH_INPUT)
    # sends texts and return button to load search results page
    search_intput.send_keys(phrase + Keys.RETURN)
    # hmmm what is this???
    # search_intput.send_keys(phrase + KeysView.RETURN)