# Generated by Django 4.2.4 on 2023-09-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aichat_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='reponse',
            new_name='response',
        ),
    ]
