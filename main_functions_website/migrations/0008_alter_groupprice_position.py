# Generated by Django 3.2.14 on 2022-07-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_functions_website', '0007_alter_groupprice_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprice',
            name='position',
            field=models.IntegerField(max_length=6),
        ),
    ]
