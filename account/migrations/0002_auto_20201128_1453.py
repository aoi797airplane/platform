# Generated by Django 3.1.3 on 2020-11-28 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ea',
        ),
        migrations.AddField(
            model_name='profile',
            name='ea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ea', verbose_name='EA'),
        ),
    ]
