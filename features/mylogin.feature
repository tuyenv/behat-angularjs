Feature: Authentication
  In order to gain access to the site management area
  As an admin
  I need to be able to login and logout

  Scenario: Logging in
    Given I am on "/login"
    And I am authenticated as "admin@example.com" using "secret"
    Then I should see "Logout"