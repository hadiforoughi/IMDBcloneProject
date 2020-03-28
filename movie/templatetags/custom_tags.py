from django import template
register = template.Library()

@register.simple_tag
def assign_to_variable(value):
    return value

