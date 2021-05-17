from django.contrib import admin
from .models import News, Category # импортируем класс приложения


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published'] # отображение полей в админке
    list_display_links = ['id', 'title']   #ссылочные поля в админке
    search_fields = ('title', 'content')   # поиск в админке только по полям title, content
    list_editable = ['is_published'] # редактирование прямо из списка
    list_filter = ['is_published', 'category'] # по каким полям мы можем фильтровать

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] # отображение полей в админке
    list_display_links = ['id', 'title']   #ссылочные поля в админке
    search_fields = ('title',)   # поиск в админке только по полям title, content

admin.site.register(News, NewsAdmin) # регистрируем класс приложения и класс NewsAdmin (порядок важен: сперва основаная модель, потом настройка)
admin.site.register(Category, CategoryAdmin)
