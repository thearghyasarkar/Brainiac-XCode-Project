# Generated by Django 4.2.5 on 2023-09-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0031_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=335300224600607515149062955408557491396, unique=True),
        ),
    ]
