from django import forms
from .models import Category, News
import re                           # для работы с регулярными выражениями
from django.core.exceptions import ValidationError

"""
class NewsForm(forms.Form):
    
    title = forms.CharField(max_length=150, label='Название:',
                            widget=forms.TextInput(attrs={"class":"form-control"})) #label - название формы на сайте, attrs - атрибуты формы

    content = forms.CharField(label='Текст:',
                              required=False,                                    #required - обязательность заполнения поля
                              widget=forms.Textarea(attrs={"class":"form-control"}))

    is_published = forms.BooleanField(label='Опубликовать',
                                      initial=True,                            #initial - начальное значение для поля
                                      widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))

    category = forms.ModelChoiceField(queryset = Category.objects.all(),    #для связей. Если без связей, то ChoiceField
                                      label='Категория:',
                                      empty_label='Выберите категорию',   #В начале списка будет не "------"
                                      widget=forms.Select(attrs={"class":"form-select"}))
"""

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'            # получение всех полей форм
        fields = ['title', 'content', 'is_published', 'category']   # получение конкретных полей форм
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class": "form-select"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):         # проверка наличия цифры в начале заголовка
            raise ValidationError('Название не должно начинаться с цифры')
        return title



