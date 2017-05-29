# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthDesign', '0008_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
    ]
