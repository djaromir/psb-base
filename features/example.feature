Feature: Python Selenium Behave base for automated web applications tests

  Scenario: Ensure that user can open browser on google
    Given  I open https://www.google.com/
    Then  The URL is https://www.google.com/
