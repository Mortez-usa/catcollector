# Generated by Django 4.1.3 on 2022-11-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cat",
            name="age",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
