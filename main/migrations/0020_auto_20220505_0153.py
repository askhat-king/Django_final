# Generated by Django 3.1.7 on 2022-05-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='from_where',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]