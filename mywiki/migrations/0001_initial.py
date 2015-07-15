# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contentId', models.IntegerField()),
                ('contentTitle', models.CharField(max_length=200)),
                ('content_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(verbose_name=b'date added')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userId', models.IntegerField()),
                ('userName', models.CharField(max_length=200)),
                ('userEmail', models.CharField(max_length=200)),
                ('userPassword', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='userId',
            field=models.ForeignKey(to='mywiki.user'),
        ),
    ]
