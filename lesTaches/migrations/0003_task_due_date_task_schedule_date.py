# Generated by Django 5.1.1 on 2024-10-04 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0002_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 11, 14, 13, 55, 938304)),
        ),
    ]
