# Generated by Django 4.2.7 on 2023-11-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_app', '0004_alter_cadastralrequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastralrequest',
            name='status',
            field=models.BooleanField(blank=True),
        ),
    ]
