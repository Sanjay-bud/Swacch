# Generated by Django 4.2 on 2023-04-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swachh', '0002_form_check_form_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='count',
            field=models.IntegerField(default=0, verbose_name='how many times the user has dumped garbage'),
        ),
    ]