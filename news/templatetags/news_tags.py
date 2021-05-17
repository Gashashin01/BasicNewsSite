from django import template

from news.models import Category

# Тут будут пользовательские теги теги

register = template.Library()

@register.simple_tag(name = 'get_list_categories') # декоратор для регистрации simple тегов;  name - псевдоним функции
def get_categories():  # пользовательский тег, который используется в шаблоне _sidebar.html
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html') # декоратор для регистрации inclusion тегов;
def show_categories(arg1='Hello', arg2='world'):
    categories = Category.objects.all()
    return {"categories":categories, "arg1":arg1, "arg2":arg2}
