# Generated by Django 3.1.5 on 2021-02-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0021_auto_20210205_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ProductViews',
        ),
    ]