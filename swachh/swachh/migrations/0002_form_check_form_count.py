# Generated by Django 4.2 on 2023-04-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swachh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phn_check', models.CharField(max_length=10, verbose_name='login_phone_number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='form',
            name='count',
            field=models.CharField(default=0, max_length=2, verbose_name='how many times the user has dumped garbage'),
        ),
    ]
