from behave import *
from selenium.webdriver.support.select import Select
import time
use_step_matcher("re")


@then("I must navigate to the LeaveList page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == "https://opensource-demo.orangehrmlive.com/index.php/leave/viewLeaveList"


@when("I fill the fields to view leavelist table")
def step_impl(context):
    """
       :type context: behave.runner.Context
       """
    context.leavelist.set_from_date('2020-01-01')
    context.leavelist.set_to_date('2020-11-30')
    context.leavelist.set_show_leave_with_status()
    context.leavelist.set_employee('')
    sub_unit = Select(context.leavelist.set_sub_unit())
    sub_unit.select_by_visible_text("All")
    context.leavelist.click_search_button()
    time.sleep(10)
