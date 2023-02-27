from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def draw_menu(type):
    template = '{template_name}.html'.format(template_name=type)
    context = {}
    return render_to_string(template, context)
