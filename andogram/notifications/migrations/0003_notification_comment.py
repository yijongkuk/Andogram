# Generated by Django 2.0.9 on 2018-12-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20181212_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
