# Generated by Django 4.2.4 on 2023-09-09 16:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat_history', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]