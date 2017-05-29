# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0021_auto_20170527_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('procedure', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('provider', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('demographics', models.ForeignKey(to='HealthDesign.Demographics')),
            ],
        ),
    ]
