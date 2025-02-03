# Generated by Django 5.1.5 on 2025-02-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilbuild', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('cmp_name', models.CharField(max_length=100)),
                ('srv_cat', models.CharField(max_length=100)),
                ('expc', models.CharField(max_length=100)),
                ('certi', models.FileField(upload_to=None)),
                ('wrk_hrs', models.CharField(max_length=100)),
            ],
        ),
    ]
