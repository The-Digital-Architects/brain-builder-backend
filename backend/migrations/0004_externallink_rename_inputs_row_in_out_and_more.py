# Generated by Django 4.2.6 on 2024-07-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_taskdescription_file_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('task_description', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='external_link', serialize=False, to='backend.taskdescription')),
                ('url', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='row',
            old_name='inputs',
            new_name='in_out',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='error_list',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='feature_names',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='network_biases',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='network_weights',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='plots',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='task_id',
        ),
        migrations.AddField(
            model_name='progress',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='progress',
            name='task_description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.taskdescription', related_name='progress'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clusteringdescription',
            name='task_description',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='clustering_description', serialize=False, to='backend.taskdescription'),
        ),
        migrations.AlterField(
            model_name='neuralnetworkdescription',
            name='task_description',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='neural_network_description', serialize=False, to='backend.taskdescription'),
        ),
    ]
