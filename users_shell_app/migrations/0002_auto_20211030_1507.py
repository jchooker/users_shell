# Generated by Django 2.2 on 2021-10-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_shell_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
