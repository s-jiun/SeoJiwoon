# Generated by Django 3.2.5 on 2021-07-21 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_idea_devtools'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='desc',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='likes',
            new_name='interest',
        ),
        migrations.RenameField(
            model_name='idea',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='devtools',
        ),
    ]
