# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0015_auto_20170527_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergies',
            name='reaction',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='careplan',
            name='instructions',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizations',
            name='instructions',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='medication',
            name='instructions',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='problemlist',
            name='age',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='problemlist',
            name='observation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='procedures',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='provider',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
