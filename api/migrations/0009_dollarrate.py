# Generated by Django 3.1.4 on 2022-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_userprofile_nasiya_foiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='DollarRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
    ]
