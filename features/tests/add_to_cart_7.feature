# Created by lubna khan at 6/22/2023
Feature: Add item to cart

  Scenario: Add item to cart
  Given I am on Amazon homepage
  When I search for 'pen'
  And Store product name
    And open item page
  And I click on an item
    And I click on 'Add to Cart' button
    And I click on 'Go to Cart' button
    Then Verify item(s) added to cart