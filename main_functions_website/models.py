from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import *


# Create your models here.

class GroupPrice(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, db_index=True)
    position = models.IntegerField(validators=[MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Группа цены'
        verbose_name_plural = 'Группы цен'

    def __str__(self):
        return f'{self.position} {self.name}'


class Price(models.Model):
    subtitle = models.CharField(max_length=200)
    price = models.CharField(max_length=15)
    group_price = models.ForeignKey(GroupPrice, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = 'цену'
        verbose_name_plural = 'цены'

    def __str__(self):
        return f'{self.subtitle} {self.price}'


class Article(models.Model):
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Основная часть')

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return f'{self.title} {self.text}'

