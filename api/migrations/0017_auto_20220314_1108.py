# Generated by Django 3.1.4 on 2022-03-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_cashboxreceive_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashboxreceive',
            name='date',
            field=models.DateField(),
        ),
    ]
