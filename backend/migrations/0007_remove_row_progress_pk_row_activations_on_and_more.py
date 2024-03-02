# Generated by Django 4.2.6 on 2024-03-02 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='progress_pk',
        ),
        migrations.AddField(
            model_name='row',
            name='activations_on',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='taskdescription',
            name='af_visibility',
            field=models.BooleanField(default=False),
        ),
    ]
