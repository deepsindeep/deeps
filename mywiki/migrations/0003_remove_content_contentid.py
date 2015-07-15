# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywiki', '0002_remove_user_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='contentId',
        ),
    ]
