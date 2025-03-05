# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg
@register.filter
def to(value):
    return range(1, value + 1)