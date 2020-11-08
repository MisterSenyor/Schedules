from django import template

register = template.Library()

def order_by(model, arg):
    try:
        return model.order_by(arg)
    except:
        return ["error"]

register.filter('order_by', order_by)