# Generated by Django 3.1.5 on 2021-02-02 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20210202_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
