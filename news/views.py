from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect # для генерации ошибки 404, если какой-то записи в базе данных нету. Или можно использовать то что выше
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


# Create your views here.

# Реализация вьюхи через класс
class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'  # кастомный шаблон. Если это не прописывать,
                                                # то по умолчанию шаблон должен называться news_list.html
    context_object_name = 'news'                # название обьекта, который будет юзаться в шаблоне. Аналог словаря context в функциях
    extra_context = {'title': 'Главная'}        # дополнительный контекст. Тоже аналог context в функциях. ДЛЯ СТАТИЧНЫЙ ДАННЫХ

    def get_context_data(self, *, object_list=None, **kwargs): # дополнительный контекст, только для ДИНАМИЧНЫЙ ДАННЫХ (ЛУЧШЕ ЮЗАТЬ ЭТО)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):                                    # фильтрация данных
        return News.objects.filter(is_published=True)


# Реализация вьюхи через функции
def index(request):
    news = News.objects.all()    # Сортировка по дате
    context = {
        'news':news,
        'title':'Список новостей',
    }
    return render(request, template_name = 'news/index.html', context = context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news':news,
        'category':category,
    }
    return render(request, template_name = 'news/category.html', context = context)

def get_post(request, news_id):
    #news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News,pk=news_id)  #то же что и сверху, только с проверкой на наличие исключения DoesNotExist
    return render(request, template_name='news/self_post.html', context = {'news_item':news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)   #получение данных из формы
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)  # если используется класс forms.Form в файле forms.py
            news = form.save()   # если используется класс forms.ModelForm в файле forms.py
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, template_name='news/add_news.html', context = {'form':form})
