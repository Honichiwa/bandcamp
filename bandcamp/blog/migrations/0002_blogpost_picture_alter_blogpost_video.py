# Generated by Django 4.2.2 on 2023-06-20 07:15

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/', verbose_name='picture'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='video'),
        ),
    ]