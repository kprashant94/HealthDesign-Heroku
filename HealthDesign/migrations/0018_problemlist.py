# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0017_auto_20170527_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observation', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('comment', models.CharField(max_length=100)),
                ('demographics', models.ForeignKey(to='HealthDesign.Demographics')),
            ],
        ),
    ]
