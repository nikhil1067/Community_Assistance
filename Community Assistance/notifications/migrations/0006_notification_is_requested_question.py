# Generated by Django 3.0.6 on 2020-07-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20200629_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_requested_question',
            field=models.BooleanField(default=False),
        ),
    ]
