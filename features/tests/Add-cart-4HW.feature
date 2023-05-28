from selenium.webdriver.common.by import By
from behave import when, then, given
# Created by lubna khan at 5/15/2023

Feature: Adding product to cart and verifying it

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Doll Tape
    When Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item