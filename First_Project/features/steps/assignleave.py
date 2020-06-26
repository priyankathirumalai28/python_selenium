import time

from behave import *
from features.factory import login_func
from selenium.webdriver.support.select import Select

use_step_matcher("re")


@given("I login to the OrangeHRMS")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    login_func(context)
    print("Login successful")

@when('I click on the "Leave"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_leave()

@when('I click on the "Assign Leave"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_assign_leave()

@when('I click on the "Quick Assign Leave"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_quick_assign_leave()

@then("I must navigate to the Assign Leave page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == "https://opensource-demo.orangehrmlive.com/index.php/leave/assignLeave"

@when('I Filling all the required fields to assign leave')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.assignleave.set_emp_name("Linda Anderson")
    leave_type = Select(context.assignleave.get_leave_type())
    leave_type.select_by_visible_text("FMLA US")
    context.assignleave.set_from_date("2020-05-01")
    context.assignleave.set_to_date("2020-05-02")
    part_days = Select(context.assignleave.get_partial_days())
    part_days.select_by_visible_text("None")
    context.assignleave.set_comment("Kindly Approve\n")
    context.browser.find_element_by_xpath("//input[@id='assignBtn']").click()
    time.sleep(4)
    context.assignleave.click_ok_confirm()
    time.sleep(5)