# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0020_problemlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedures',
            name='demographics',
        ),
        migrations.DeleteModel(
            name='Procedures',
        ),
    ]
