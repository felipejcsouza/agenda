# Generated by Django 3.0.6 on 2020-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200525_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(default='online', max_length=100),
            preserve_default=False,
        ),
    ]
