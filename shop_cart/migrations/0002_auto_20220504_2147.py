# Generated by Django 3.1.7 on 2022-05-04 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20220504_2147'),
        ('shop_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcartitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
    ]
