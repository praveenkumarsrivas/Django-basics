# Generated by Django 3.0.8 on 2020-08-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('rate', models.CharField(max_length=2)),
                ('suggestion', models.TextField()),
                ('best', models.TextField()),
                ('worst', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
