# Generated by Django 4.2.5 on 2023-09-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_user_address_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=320140326131669321956930591845953427652, unique=True),
        ),
    ]
