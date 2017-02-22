from django import template
import pprint

register = template.Library()

@register.filter(name='console')
def print_console(item,arg=None):
    if arg:
        item = item[int(arg)]
    print("Type:",type(item))
    pp = pprint.PrettyPrinter(indent=4)
    print("Value:")
    pp.pprint(item)
    return item
