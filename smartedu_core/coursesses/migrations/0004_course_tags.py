# Generated by Django 5.0.6 on 2024-05-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesses', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='coursesses.tag'),
        ),
    ]
