# Generated by Django 3.1.4 on 2022-04-09 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20220408_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakturaitem',
            name='name',
        ),
        migrations.AlterField(
            model_name='receiveitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receive_items', to='api.productfilial'),
        ),
    ]
