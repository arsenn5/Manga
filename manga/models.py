from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Type(models.Model):
    title = models.CharField(choices=(
        ('manga', 'manga'),
        ('manhwa', 'manhva'),
        ('comics', 'comics'),
    ), max_length=50)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(choices=(
        ('боевик', 'боевик'),
        ('боевые искусства', 'боевые искусства'),
        ('героическое фэнтези', 'героическое фэнтези'),
        ('детектив', 'детектив'),
        ('дзёсэй', 'дзёсэй'),
        ('драма', 'драма'),
        ('комедия', 'комедия'),
        ('научная фантастика', 'научная фантастика'),
        ('приключения', 'приключения'),
        ('романтика ', 'романтика '),
        ('ужасы ', 'ужасы '),
        ('спорт ', 'спорт '),
    ), max_length=100)

    def __str__(self):
        return self.name


class Manga(models.Model):
    ru_name = models.CharField(max_length=100, null=True)
    eng_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    year = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField(Genre,    null=True)
    synopsis = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.ru_name}'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    text = models.TextField("Сообщение", max_length=5000)
    manga = models.ForeignKey(Manga, verbose_name="манга", on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return f"{self.manga}"
