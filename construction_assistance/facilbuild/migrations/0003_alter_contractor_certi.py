# Generated by Django 5.1.5 on 2025-02-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilbuild', '0002_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='certi',
            field=models.FileField(upload_to=''),
        ),
    ]
