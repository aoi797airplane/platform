# Generated by Django 3.1.3 on 2020-11-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_ea_ea'),
        ('account', '0004_profile_ea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ea',
            field=models.ManyToManyField(blank=True, to='main.Ea', verbose_name='EA'),
        ),
    ]
