from behave import *

use_step_matcher("parse")


@then("The URL is {url}")
def step_impl(context, url):
    assert context.driver.current_url == url


@step("I open {url}")
def step_impl(context, url):
    context.driver.get(url)
