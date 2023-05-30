# Created by lubna khan at 5/15/2023
Feature: Finding the main categories on the Best Sellers page
  # Enter feature description here

  Scenario: Verify that Bestsellers page shows five categories
    Given Open Amazon Best seller
    Then Verify that Best Sellers has 5 links
#    Then Verify that Best Sellers has 5 links