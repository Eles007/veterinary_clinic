# Generated by Django 3.2.14 on 2022-07-19 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_functions_website', '0010_alter_groupprice_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprice',
            name='position',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
