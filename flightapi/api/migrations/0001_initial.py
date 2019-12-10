# Generated by Django 3.0 on 2019-12-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('flightID', models.TextField()),
                ('flightNum', models.TextField()),
                ('scheduledOriginGate', models.TextField()),
                ('scheduledDestinationGate', models.TextField()),
                ('outGMT', models.DateTimeField()),
                ('inGMT', models.DateTimeField()),
                ('offGMT', models.DateTimeField()),
                ('onGMT', models.DateTimeField()),
                ('destination', models.TextField()),
                ('origin', models.TextField()),
                ('destinationFullName', models.TextField()),
                ('originFullName', models.TextField()),
            ],
        ),
    ]