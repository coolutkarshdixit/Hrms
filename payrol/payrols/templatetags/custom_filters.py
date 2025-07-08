from django import template

register = template.Library()

@register.filter
def get_value(dictionary, key):
    """Return value from dictionary or empty string if key missing"""
    return dictionary.get(key, "")
