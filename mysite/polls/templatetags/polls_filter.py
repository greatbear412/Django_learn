from django import template

register = template.Library()

@register.filter
def cuty(value,arg):  # 过滤器函数只能接受一个自定义参数
    return value.replace(arg,' ')