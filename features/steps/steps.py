from behave import given, when, then
from pathFinder.helpers import *


@given('my starting point is {origin}')
def set_origin(context, origin):
    context.origin = origin


@given('my destination point is {destination}')
def set_destination(context, destination):
    context.destination = destination


@when('I look for one of the shortest path')
def find_shortest_path(context):
    context.result = calculate_path(context.origin, context.destination)


@then('the path is one of the following ones')
def check_result(context):
    combinations = set()
    for row in context.table:
        combinations.add(row["combination"])

    assert context.result in combinations
