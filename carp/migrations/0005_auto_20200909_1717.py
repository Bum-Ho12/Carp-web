# Generated by Django 3.0.8 on 2020-09-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carp', '0004_auto_20200909_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]