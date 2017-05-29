# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0010_auto_20170527_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allergy_name', models.CharField(max_length=20)),
                ('reaction', models.TextField(max_length=200)),
                ('severity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('instructions', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Encounters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encounter', models.CharField(max_length=20)),
                ('provider', models.CharField(max_length=20)),
                ('location', models.TextField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Immunizations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('immunizations_name', models.CharField(max_length=20)),
                ('type', models.TextField(max_length=50)),
                ('dose_quantity', models.CharField(max_length=20)),
                ('instructions', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('type', models.TextField(max_length=50)),
                ('medication_name', models.CharField(max_length=20)),
                ('instructions', models.TextField(max_length=200)),
                ('dose_quantity', models.CharField(max_length=20)),
                ('rate_quantity', models.CharField(max_length=20)),
                ('prescriber_name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('observation', models.TextField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('age', models.TextField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('procedure', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('organization_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='demographics',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='provider',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='procedures',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='problemlist',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='medication',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='immunizations',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='encounters',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='careplan',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
        migrations.AddField(
            model_name='allergies',
            name='demographics',
            field=models.ForeignKey(to='HealthDesign.Demographics'),
        ),
    ]
