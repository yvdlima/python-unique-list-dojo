from src.lists import UniqueList
from behave import given, when, then

def add_itens_to_uniquelist(uniquelist, qtd, prefix="text"):
    for i in range(qtd):
        uniquelist.append(f"{prefix}{i}")

@given('a new unique list')
def step_impl(context):
    context.list = UniqueList()

    assert isinstance(context.list, UniqueList)

@when('we add a null/empty string to the list')
def step_impl(context):
    context.list.append("")
    context.list.append(None)

@then('the list should ignore and be empty')
def step_impl(context):
    assert len(context.list) is 0

@given('another new unique empty list')
def step_impl(context):
    context.list = UniqueList()
    #context.execute_steps("the list should ignore and be empty")

@when('we add {qtd:d} itens')
def step_impl(context, qtd):
    assert qtd > 1
    add_itens_to_uniquelist(context.list, qtd)

@then('the first added item is the first in the list and the last added item is the last')
def step_impl(context):
    last_ind = len(context.list) - 1

    assert context.list[0] == "text0"
    assert context.list[last_ind] == f"text{last_ind}"

#This should be tested first OR not tested at all.
@then('the list can be looked up by index counting from 0')
def step_impl(context):
    pass#Done in the previous test...

@given('a new list with some itens')
def step_impl(context):
    context.list = UniqueList()
    add_itens_to_uniquelist(context.list, 5)

@when('we add a item which was already in the list and not in the last position')
def step_impl(context):
    context.list.append("text0")

@then('the item will not be duplicated and instead will go to the last position')
def step_impl(context):
    assert context.list.index("text0") is (len(context.list) - 1)

@given('we have a list with {qtd_items:d} items with max length of {list_length:d}')
def step_impl(context, qtd_items, list_length):
    context.list = UniqueList(list_length)
    context.max_length = list_length
    context.qtd_diff = list_length - qtd_items
    add_itens_to_uniquelist(context.list, qtd_items)

@when('we add more itens then the list length')
def step_impl(context):
    add_itens_to_uniquelist(context.list, context.qtd_diff + 2, "newtext")

@then('the first itens should be removed and the new items inserted')
def step_impl(context):
    last_ind = len(context.list)-1

    assert context.list[0] != "text0"
    assert context.list[last_ind].startswith("newtext")
