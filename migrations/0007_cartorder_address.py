# Generated by Django 4.0.3 on 2022-04-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_useraddressbook_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
