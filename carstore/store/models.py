from django.db import models


class ad_car(models.Model):
    mark = models.CharField(max_length=255, verbose_name='Марка', null=True)
    mod = models.CharField(max_length=255, verbose_name='Модель', null=True)
    year = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    millage = models.PositiveIntegerField(verbose_name='Пробег')
    owners = models.PositiveSmallIntegerField(verbose_name='Кол-во владельцев')
    images = models.ImageField(upload_to='photos', verbose_name='Фото', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    description = models.TextField(null=True, verbose_name='Описание')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

