# Generated by Django 3.1.1 on 2020-10-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content_a',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_b',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_c',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_d',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_e',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_f',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_content_g',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(blank=True),
        ),
    ]
