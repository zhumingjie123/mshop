# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userid', models.PositiveIntegerField()),
                ('pollid', models.PositiveIntegerField()),
                ('vote_date', models.DateField()),
            ],
        ),
    ]
