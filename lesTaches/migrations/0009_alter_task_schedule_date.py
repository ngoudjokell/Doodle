# Generated by Django 5.1.1 on 2024-10-10 01:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0008_alter_task_schedule_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 17, 2, 51, 25, 343681)),
        ),
    ]
