from django import template

register = template.Library()

@register.filter
def dollar_sign(price):
    if price:
        return '$' * price
    else:
        return price
