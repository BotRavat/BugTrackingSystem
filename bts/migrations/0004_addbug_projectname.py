# Generated by Django 4.0 on 2022-02-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0003_remove_addbug_projectname'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbug',
            name='projectname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
