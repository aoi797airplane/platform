# Generated by Django 3.1.3 on 2020-11-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_ea_ea'),
        ('account', '0003_remove_profile_ea'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ea',
            field=models.ManyToManyField(to='main.Ea'),
        ),
    ]