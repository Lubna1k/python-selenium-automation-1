from behave import when, then


@when("Select computers department")
def select_computers_department(context):
    context.app.header.select_computers_department()


@then("Verify the correct department is displayed")
def verify_department(context):
    context.app.amazon_departments.verify_department()