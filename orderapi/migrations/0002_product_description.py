# Generated by Django 4.0.1 on 2022-04-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='product is good', max_length=20000),
        ),
    ]
