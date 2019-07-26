from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag
def querystring(prefix=True, **kwargs):
    return ('?' if prefix else '') + urlencode(kwargs)