# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-13 14:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MILK', '0022_remove_transaction_itemquantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='itemID',
        ),
    ]
