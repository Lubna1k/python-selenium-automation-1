# Created by lubna khan at 7/6/2023

  Feature: Amazon find elements

  @smoke
  Scenario: Verify the user sees 5 links on the best sellers page
    Given Open amazon main page
    When Click Best Sellers
    Then Verify links displayed

