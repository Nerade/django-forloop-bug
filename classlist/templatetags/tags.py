from django import template

from classlist.utils import get_class_list

register = template.Library()

@register.inclusion_tag('tag.html', takes_context=True)
def create_class_list(context):
    return {'available_class_list':get_class_list(),
            }
