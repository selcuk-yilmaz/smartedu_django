# Generated by Django 5.0.6 on 2024-05-29 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesses', '0004_course_tags'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]