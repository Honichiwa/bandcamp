# Generated by Django 4.2.2 on 2023-06-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0002_rename_conert_concert'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concert',
            options={'verbose_name': 'concert', 'verbose_name_plural': 'concerts'},
        ),
    ]
