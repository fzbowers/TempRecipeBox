# Generated by Django 4.1.1 on 2022-11-08 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_ingredient_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
    ]
