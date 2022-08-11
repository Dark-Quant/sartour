# Generated by Django 4.0.4 on 2022-08-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_stream', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='video_vr',
        ),
        migrations.AlterField(
            model_name='tour',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='video_stream.video'),
        ),
    ]
