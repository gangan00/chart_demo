# Generated by Django 3.0.8 on 2020-07-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdata', '0002_auto_20200711_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartinfo',
            name='AB',
            field=models.CharField(max_length=2000, null=True, verbose_name='AB：专利摘要'),
        ),
    ]
