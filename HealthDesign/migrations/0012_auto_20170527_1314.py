# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0011_auto_20170527_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergies',
            name='allergy_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='careplan',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='ethnicity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='encounters',
            name='encounter',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encounters',
            name='location',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='encounters',
            name='provider',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='role',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='immunizations',
            name='dose_quantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='immunizations',
            name='immunizations_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medication',
            name='dose_quantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medication',
            name='medication_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medication',
            name='prescriber_name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medication',
            name='rate_quantity',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='problemlist',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='procedures',
            name='organization_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='procedures',
            name='procedure',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
