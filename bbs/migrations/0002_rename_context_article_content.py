# Generated by Django 4.1 on 2024-05-07 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='context',
            new_name='content',
        ),
    ]