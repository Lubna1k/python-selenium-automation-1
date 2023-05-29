# Created by lubna khan at 5/29/2023
Feature: Product Search

  Scenario: Verify all products on search page have a picture and a name
    Given I am on Amazon homepage
    When I search for 'Tshirt'
    Then verify products have picture and name
    Then Verify all colors are clickable
    Then Print verification results