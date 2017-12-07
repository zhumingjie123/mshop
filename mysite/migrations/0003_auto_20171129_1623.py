# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_votecheck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollitem',
            name='poll',
        ),
        migrations.DeleteModel(
            name='VoteCheck',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='PollItem',
        ),
    ]
