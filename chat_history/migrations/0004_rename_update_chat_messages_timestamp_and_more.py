# Generated by Django 4.2.2 on 2023-09-13 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_history', '0003_chat_messages_transcript_delete_transaction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat_messages',
            old_name='update',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='transcript',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='chat_messages',
            name='created_at',
        ),
    ]