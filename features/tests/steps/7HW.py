from behave import *

use_step_matcher("re")


@then('Verify "Your Shopping Cart is empty"  text present')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify "Your Shopping Cart is empty"  text present')


@then("Verify 'Your Shopping Cart is empty\.' text present")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify \'Your Shopping Cart is empty.\' text present')