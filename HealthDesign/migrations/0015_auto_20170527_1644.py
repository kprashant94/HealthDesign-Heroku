# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0014_auto_20170527_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounters',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]
