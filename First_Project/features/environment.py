from selenium import webdriver
from features.browser import Browser
from features.pages.login import LoginPage
from features.pages.home import HomePage
from features.pages.assignleave import LeavePage
from features.pages.leavelist import LeaveList
from features.pages.home_time import TimePage


def before_all(context):
    browser_obj = Browser()
    context.browser = browser_obj.get_driver()
    context.login = LoginPage(context.browser)
    context.home = HomePage(context.browser)
    context.assignleave = LeavePage(context.browser)
    context.leavelist = LeaveList(context.browser)
    context.time = TimePage(context.browser)
    print("Executing before all block")


# def before_feature(context, feature):
#      print("Before feature\n")

# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


# def after_feature(context,feature):
#      print("\nAfter feature")
#
def after_all(context):
    print('**************Executing after all block*****************')
    context.browser.quit()
