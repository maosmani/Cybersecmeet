# Generated by Django 3.2.6 on 2021-10-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_newuser_admin_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='admin_key',
            field=models.IntegerField(blank=True, max_length=150),
        ),
    ]
