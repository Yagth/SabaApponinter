# Generated by Django 4.0.3 on 2022-03-12 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0011_hairsalon_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hairsalon',
            name='name',
        ),
    ]
