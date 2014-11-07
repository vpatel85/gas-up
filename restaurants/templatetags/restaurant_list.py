from django import template

register = template.Library()

@register.filter
def dollar_sign(price):
    if price:
        return '<span class="glyphicon glyphicon-usd"></span>' * price
    else:
        return price
