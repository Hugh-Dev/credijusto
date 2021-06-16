# Generated by Django 3.2.4 on 2021-06-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TokenModel',
            fields=[
                ('token', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('life', models.IntegerField(default=5)),
            ],
            options={
                'verbose_name': 'TokenModel',
                'verbose_name_plural': 'TokenModels',
                'ordering': ['token'],
            },
        ),
    ]
