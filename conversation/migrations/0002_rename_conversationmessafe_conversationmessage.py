# Generated by Django 4.2.10 on 2024-02-25 06:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConversationMessafe',
            new_name='ConversationMessage',
        ),
    ]
