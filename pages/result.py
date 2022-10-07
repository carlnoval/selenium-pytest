"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

# manually entered from course
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

  RESULT_LINKS = (By.XPATH, "//a[@data-testid='result-title-a']")
  SEARCH_INPUT = (By.ID, "search_form_input")

  # dunder init method constructor
  def __init__(self, browser):
    self.browser = browser

  def result_link_titles(self):
    # TODO
    return []
  
  def search_input_value(self):
    # TODO
    return ""

  def title(self):
    # TODO
    return ""
