# Generated by Django 2.0.5 on 2018-05-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
