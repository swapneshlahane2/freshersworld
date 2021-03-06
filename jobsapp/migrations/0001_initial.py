# Generated by Django 3.0.6 on 2020-06-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgricultureJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('vaccancy', models.IntegerField()),
                ('experience', models.FloatField()),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PharmaJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('vaccancy', models.IntegerField()),
                ('experience', models.FloatField()),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('vaccancy', models.IntegerField()),
                ('experience', models.FloatField()),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
    ]
