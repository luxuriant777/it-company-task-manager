# Generated by Django 4.1.3 on 2022-11-12 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="worker",
            options={
                "ordering": ["first_name"],
                "verbose_name": "worker",
                "verbose_name_plural": "workers",
            },
        ),
    ]