# Generated by Django 4.2.7 on 2023-12-09 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_chegue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='thing',
        ),
        migrations.RemoveField(
            model_name='pos_order',
            name='order',
        ),
        migrations.RemoveField(
            model_name='pos_order',
            name='thing',
        ),
        migrations.DeleteModel(
            name='Chegue',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Pos_order',
        ),
    ]
