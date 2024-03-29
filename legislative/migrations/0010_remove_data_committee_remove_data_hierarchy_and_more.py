# Generated by Django 4.1.12 on 2024-01-26 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0009_remove_data_committee_remove_data_hierarchy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='data',
            name='hierarchy',
        ),
        migrations.RemoveField(
            model_name='data',
            name='subcommittee',
        ),
        migrations.RemoveField(
            model_name='data',
            name='title',
        ),
        migrations.AddField(
            model_name='data',
            name='committee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legislative.committees'),
        ),
        migrations.AddField(
            model_name='data',
            name='hierarchy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legislative.hierarchy'),
        ),
        migrations.AddField(
            model_name='data',
            name='subcommittee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legislative.subcommittees'),
        ),
        migrations.AddField(
            model_name='data',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legislative.title'),
        ),
    ]
