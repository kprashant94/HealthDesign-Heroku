# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0009_remove_album_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('martial_status', models.CharField(max_length=10)),
                ('religious_affiliation', models.CharField(max_length=10)),
                ('ethnicity', models.CharField(max_length=20)),
                ('language_spoken', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('telephone', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('telephone', models.CharField(max_length=15)),
                ('demographics', models.ForeignKey(to='HealthDesign.Demographics')),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
