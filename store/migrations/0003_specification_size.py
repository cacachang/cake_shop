# Generated by Django 5.0.6 on 2024-05-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_name_product_name_specification_flavor'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='size',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]