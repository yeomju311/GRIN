# Generated by Django 3.1.1 on 2020-09-15 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20200914_2358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='Content',
            new_name='content',
        ),
    ]