# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-21 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classlist', '0002_auto_20170221_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='a',
            name='case',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='classlist.Case'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='b',
            name='case',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classlist.Case'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c',
            name='case',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classlist.Case'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='d',
            name='case',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='classlist.Case'),
            preserve_default=False,
        ),
    ]
