# Generated by Django 2.2.16 on 2022-05-24 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220525_0106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='%(app_label)s_%(class)s_name_unique',
        ),
    ]
