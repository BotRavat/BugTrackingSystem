# Generated by Django 4.0 on 2022-02-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0004_addbug_projectname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbug',
            name='projectname',
            field=models.CharField(default='testproject', max_length=100),
        ),
    ]
