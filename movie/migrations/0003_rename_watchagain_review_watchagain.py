# Generated by Django 4.0 on 2023-07-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='watchagain',
            new_name='watchAgain',
        ),
    ]