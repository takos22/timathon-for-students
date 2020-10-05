# Generated by Django 3.1.2 on 2020-10-05 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
    ]
