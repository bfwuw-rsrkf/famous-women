from django import forms
from women.models import Category, Woman


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Имя')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Не выбрано')
#     content = forms.CharField(label='Биография')
#     slug = forms.SlugField(max_length=255)
#     is_published = forms.BooleanField(required=False, label='Опубликовать')


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Woman
        fields = [
            'title',
            'cat',
            'content',
            'slug',
            'is_published'
        ]
