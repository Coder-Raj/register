# Generated by Django 2.0 on 2019-06-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190609_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Status',
            field=models.CharField(default='Insert', max_length=20),
        ),
    ]
