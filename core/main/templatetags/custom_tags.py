from django import template
import math

register = template.Library()

@register.filter
def func(num):
    rating = []
    for i in range(math.floor(num)):
        rating.append(i)
    return rating
