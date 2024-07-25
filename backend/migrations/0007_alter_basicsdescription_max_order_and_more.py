# Generated by Django 4.2.6 on 2024-07-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_remove_clusteringdescription_model_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicsdescription',
            name='max_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicsdescription',
            name='min_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicsdescription',
            name='type_menu_options',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clusteringdescription',
            name='type_selection_options',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='dataset',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='file_name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='function_name',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='n_inputs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='n_outputs',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]