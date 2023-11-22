# Generated by Django 4.2.6 on 2023-11-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('study', models.CharField(max_length=255)),
                ('registration_no', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=50)),
                ('experience_years', models.PositiveIntegerField()),
                ('speciality', models.CharField(max_length=100)),
                ('profile', models.TextField()),
            ],
        ),
    ]
