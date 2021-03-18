# Generated by Django 3.0.8 on 2020-09-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carp', '0005_auto_20200909_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('c1', models.FileField(blank=True, null=True, upload_to='')),
                ('c2', models.FileField(blank=True, null=True, upload_to='')),
                ('c3', models.FileField(blank=True, null=True, upload_to='')),
                ('c4', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=600)),
            ],
        ),
    ]