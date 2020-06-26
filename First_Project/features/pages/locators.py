class Locators:
    # Login page objects
    txtbox_username_xpath = "//*[@id='txtUsername']"
    txtbox_password_xpath = "//input[@id='txtPassword']"
    btn_login_xpath = "//input[@id='btnLogin']"
    span_invalid_info_xpath = "//span[@id='spanMessage']"

    # Home page objects
    btn_welcome_xpath = "//a[@id='welcome']"
    btn_logout_xpath = "//a[contains(text(),'Logout')]"
    span_leave_xpath = "//*[@id='menu_leave_viewLeaveModule']"
    span_assign_leave_xpath = "//*[@id='menu_leave_assignLeave']"
    span_quick_assign_leave_xpath = "//*[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td[1]/div/a/span"

    # Home - Time page object
    span_time_xpath = "//*[@id='menu_time_viewTimeModule']"
    span_time_attendance_xpath = '//*[@id="menu_attendance_Attendance"]'
    span_time_attendance_employee_report_xpath = '//*[@id="menu_attendance_viewAttendanceRecord"]'
    span_time_project_info_xpath = '//*[@id="menu_admin_ProjectInfo"]'
    span_time_project_customers_xpath = '//*[@id="menu_admin_viewCustomers"]'

    # Leave list Objects
    span_from_date_leave_list_xpath = '// *[ @ id = "calFromDate"]'
    span_to_date_leave_list_xpath = '//*[@id="calToDate"]'
    span_show_leave_with_status_all_xpath = '//*[@id="leaveList_chkSearchFilter_checkboxgroup_allcheck"]'
    span_employee_xpath = '//*[@id="leaveList_txtEmployee_empName"]'
    span_sub_unit_xpath = '//*[@id="leaveList_cmbSubunit"]  '
    span_include_past_employee_xpath = '//*[@id="leaveList_cmbWithTerminated"]'
    btn_search_leave_list_xpath = '//*[@id="btnSearch"]'
    btn_reset_leave_list_xpath = '//*[@id="btnReset"]'

    # Leave page objects
    txt_emp_name_xpath = "//input[@id='assignleave_txtEmployee_empName']"
    ddl_leave_type_xpath = "//select[@id='assignleave_txtLeaveType']"
    date_pick_from_date_xpath = "//input[@id='assignleave_txtFromDate']"
    date_pick_to_date_xpath = "//input[@id='assignleave_txtToDate']"
    ddl_part_days_xpath = "//select[@id='assignleave_partialDays']"
    txt_area_comment_xpath = "//textarea[@id='assignleave_txtComment']"
    btn_assign_xpath = "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input"
    btn_confirm_ok_xpath = "//input[@id='confirmOkButton']"

    # Time - Attendance object
    txt_employee_name_attendance_xpath = '//*[@id="attendance_employeeName_empName"]'
    date_pick_date_attendance_xpath = '//*[@id="attendance_date"]'
    btn_view_attendance_xpath = '//*[@id="btView"]'
