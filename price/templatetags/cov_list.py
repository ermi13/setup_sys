from django import template

register = template.Library()

@register.filter
def toList(value):
    return value.split(':')