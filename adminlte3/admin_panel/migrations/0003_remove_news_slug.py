# Generated by Django 4.1 on 2022-08-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_alter_news_slug_alter_tag_name_alter_tag_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
