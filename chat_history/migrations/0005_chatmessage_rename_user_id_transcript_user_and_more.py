# Generated by Django 4.2.4 on 2023-09-15 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_history', '0004_rename_update_chat_messages_timestamp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_response', models.TextField()),
                ('ai_response', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='transcript',
            old_name='user_id',
            new_name='user',
        ),
        migrations.DeleteModel(
            name='chat_messages',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='transcript',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_history.transcript'),
        ),
    ]