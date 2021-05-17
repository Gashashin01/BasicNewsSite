from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name = 'Картинка', blank=True) # blank=True - поле необязательное
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликован?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория') # не понял почему, но когда создаешь новое поле в заполненной таблице, то надо писать null=True

    def get_absolute_url(self):  # метод можно называть по разному. Но если назвать его так, то в админке появиться кнопка "Смотреть на сайте"
        return reverse('post', kwargs={"news_id": self.pk})  # reverse - тоже самое что и тэг url в index.html ГЛЯНЬ УРОК 21

    # Метод для вывода поля title любого объекта класса News при чтении из БД. Строковое предстваление объекта
    def __str__(self):
        return self.title

    # все что ниже - для админки и шаблона
    class Meta:
        verbose_name = 'Новость'  # наименование модели в единственном числе
        verbose_name_plural = 'Новости'  # наименование модели во множественном числе
        ordering = ['-created_at', 'title']  # сортировка




class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий') # db_index - индексирует поле, делает его более быстрым для поиска

    def get_absolute_url(self):    # метод можно называть по разному. Но если назвать его так, то в админке появиться кнопка "Смотреть на сайте"
        return reverse('category', kwargs={"category_id": self.pk})  #r everse - тоже самое что и тэг url в index.html ГЛЯНЬ УРОК 21


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
