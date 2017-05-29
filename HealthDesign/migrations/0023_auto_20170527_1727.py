# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0022_procedures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographics',
            name='language_spoken',
            field=models.CharField(max_length=50),
        ),
    ]
