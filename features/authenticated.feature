Feature: Authentication
  In order to gain access to the site management area
  As an admin
  I need to be able to login and logout

  Scenario: Logging in
    Given I am on "/login"
    When I am wait for the page to be loaded "10"
    When I fill in the following:
      | username | admin@example.com |
      | passwd | secret |
    And I press "login"
    Then I should be on "/admin/"
    And I should see "Logout"