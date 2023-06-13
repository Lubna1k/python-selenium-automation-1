# Created by lubna khan at 6/13/2023
Feature: Add to cart item
  Feature: Add item to cart
  Scenario: Add item to cart
   Given I am on Amazon homepage
   When I search for 'Pen'
  And Store product name
   And I click on an item
   And I click on 'Add to Cart' button
   And I click on 'Go to Cart' button

