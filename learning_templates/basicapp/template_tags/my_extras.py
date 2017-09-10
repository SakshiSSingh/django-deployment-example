from django import template

register = template.Library()
@register.filter(name="cut")
def cut(value,arg):
    """
this cuts out all the values of "arg" from the string !

    """
    return value.replace(arg,'')

# register.filter('cut',cut) #the name by which we want to address the function  , and the function itself
