from django.template.base import Library
from django import template
from django.template.base import Node


class SetVarNode(Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        page = context['__CACTUS_CURRENT_PAGE__']
        context[self.var_name] = page.final_url

        return u""

def insert_current_page(parser, token):
    """
    {% insert_current_page varname %}
    Places the current url in the provided variable
    """

    parts = token.split_contents()
    if len(parts) != 2:
        raise template.TemplateSyntaxError("'insert_current_page' tag must be of the form: {% insert_current_page <var_name>  %}")

    return SetVarNode(parts[1])



def preBuild(site):
    register = template.Library()
    register.tag("insert_current_page", insert_current_page)
    template.base.builtins.append(register)
