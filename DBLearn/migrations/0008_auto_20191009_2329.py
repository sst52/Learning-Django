# Generated by Django 2.2.6 on 2019-10-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBLearn', '0007_auto_20191009_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]