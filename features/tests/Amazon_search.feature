# Created by lubna khan at 7/6/2023
Feature: Amazon search tests

  @smoke
  Scenario: User can search on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results for "table"
  Scenario: Verify a user can search in a department
    Given Open amazon main page
    When Select department Health & Personal Care
    When Search for Candle
    Then Verify correct department shown