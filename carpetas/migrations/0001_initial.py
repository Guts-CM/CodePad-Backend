# Generated by Django 5.1.1 on 2024-10-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carpetas',
            fields=[
                ('carpetas_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=80, null=True)),
                ('ico_url', models.CharField(max_length=40, null=True)),
            ],
            options={
                'db_table': 'carpetas',
                'managed': False,
            },
        ),
    ]
