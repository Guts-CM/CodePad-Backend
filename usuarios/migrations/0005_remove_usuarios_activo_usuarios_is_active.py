# Generated by Django 5.1.2 on 2024-10-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_usuarios_is_active_remove_usuarios_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='activo',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
