# Created by lubna khan at 6/5/2023
  Feature: Logged out user sees Sign in page when clicking Orders
Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present