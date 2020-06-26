Feature: List Of leave Of an employee
  Testing For LeaveList To Employee

#  Scenario: Testing For LeaveList To Employee
#    Given I login to the OrangeHRMS
#    When  I click on the "Leave"
#    Then I must navigate to the LeaveList page

  Scenario: Test  To View LeaveList To Employee
    Given I login to the OrangeHRMS
    When  I click on the "Leave"
    And I fill the fields to view leavelist table
    Then I must navigate to the LeaveList page