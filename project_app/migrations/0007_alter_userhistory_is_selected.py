# Generated by Django 4.2.3 on 2023-07-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0006_userhistory_is_reject_userhistory_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='is_selected',
            field=models.BooleanField(default='False'),
        ),
    ]