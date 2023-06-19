# Generated by Django 4.2.2 on 2023-06-19 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categorys', to='merch.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'sub_category',
                'verbose_name_plural': 'sub_categorys',
            },
        ),
    ]
