# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-11 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('MILK', '0008_remove_groupdetail_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='groupBuying',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
