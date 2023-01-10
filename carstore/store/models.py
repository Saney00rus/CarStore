from django.contrib.auth.models import User
from django.db import models


class ad_car(models.Model):
    mark = models.CharField(max_length=255, verbose_name='Марка')
    mod = models.CharField(max_length=255, verbose_name='Модель')
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    millage = models.PositiveIntegerField(verbose_name='Пробег')
    owners = models.PositiveSmallIntegerField(verbose_name='Кол-во владельцев')
    images = models.ImageField(upload_to='photos', verbose_name='Фото', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    description = models.TextField(null=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
