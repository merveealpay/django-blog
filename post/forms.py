from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
