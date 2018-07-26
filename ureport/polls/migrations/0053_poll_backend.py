# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 13:36
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def populate_poll_backend(apps, schema_editor):
    Poll = apps.get_model("polls", "Poll")
    Org = apps.get_model("orgs", "Org")

    for org in Org.objects.all():
        backend = org.backends.filter(slug="rapidpro").first()
        Poll.objects.filter(org=org).update(backend=backend)


class Migration(migrations.Migration):

    dependencies = [("orgs", "0025_auto_20180322_1415"), ("polls", "0052_remove_poll_backend")]

    operations = [
        migrations.AddField(
            model_name="poll",
            name="backend",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="orgs.OrgBackend"),
        ),
        migrations.RunPython(populate_poll_backend),
    ]
