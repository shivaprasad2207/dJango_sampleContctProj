# Generated by Django 2.0.6 on 2018-06-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(blank=True, max_length=255)),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('contactAdress', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
