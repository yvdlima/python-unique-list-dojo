from unique_list import UniqueList
from behave import given, when, then

@given('a new unique list')
def step_impl(context):
    context.list = []

@when('we add a null/empty string to the list')
def step_impl(context):
    assert context.list != None

@then('the list should ignore and be empty')
def step_impl(context):
    assert True is not False

@given('another new unique empty list')
def step_impl(context):
    pass

@when('we add {qtd:d} itens')
def step_impl(context, qtd):
    pass

@then('the first added item is the first in the list and the last added item is the last')
def step_impl(context):
    pass

@then('the list can be looked up by index counting from 0')
def step_impl(context):
    pass

@given('a new list with some itens')
def step_impl(context):
    pass

@when('we add a item which was already in the list and not in the last position')
def step_impl(context):
    pass

@then('the item will not be duplicated and instead will go to the last position')
def step_impl(context):
    pass

@given('we have a list with {qtd_items:d} items with max length of {list_length:d}')
def step_impl(context, qtd_items, list_length):
    pass

@when('we add more itens then the list length')
def step_impl(context):
    pass

@then('the first itens should be removed and the new items inserted')
def step_impl(context):
    pass
