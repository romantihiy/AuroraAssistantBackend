# Generated by Django 4.0.1 on 2022-01-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blockedlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedlist',
            name='ips',
            field=models.TextField(help_text='Вводите IP-адреса через пробел без запятых'),
        ),
    ]