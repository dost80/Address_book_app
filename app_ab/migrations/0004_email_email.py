# Generated by Django 2.0.2 on 2018-02-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ab', '0003_auto_20180226_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]