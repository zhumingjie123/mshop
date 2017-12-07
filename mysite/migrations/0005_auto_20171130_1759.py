# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=filer.fields.file.FilerFileField(related_name='product_image', to='filer.File'),
        ),
    ]
