# Generated by Django 3.0.8 on 2020-09-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carp', '0008_auto_20200911_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='date',
        ),
        migrations.AddField(
            model_name='notification',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
