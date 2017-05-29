# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0013_auto_20170527_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='prescriber_name',
            field=models.CharField(max_length=50),
        ),
    ]
