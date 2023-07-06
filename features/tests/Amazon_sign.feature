# Created by lubna khan at 7/6/2023
  #9______HW
Feature: Amazon Sign in page
  Scenario: Unregistered user is transferred to Sign in page
    Given Open amazon main page
    When Click Orders
    Then Verify Sign in page opened


  @smoke
  Scenario: Signin page can be opened from Signin popup
    Given Open amazon main page
    When Click on button from Signin popup
    Then Verify Sign in page opened
  Scenario: Amazon user sees sign in button
    Given Open amazon main page
    When Verify sign in is clickable
    When Wait for 5 sec
    Then Verify sign in disappears