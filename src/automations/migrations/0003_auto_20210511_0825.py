# Generated by Django 3.1.8 on 2021-05-11 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0002_auto_20210506_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='automationtaskmodel',
            name='requires_interaction',
            field=models.BooleanField(default=False, verbose_name='Requires interaction'),
        ),
        migrations.AlterField(
            model_name='automationmodel',
            name='automation_class',
            field=models.CharField(max_length=256, verbose_name='Process class'),
        ),
        migrations.AlterField(
            model_name='automationmodel',
            name='data',
            field=models.JSONField(default=dict, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='automationmodel',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='Finished'),
        ),
        migrations.AlterField(
            model_name='automationmodel',
            name='paused_until',
            field=models.DateTimeField(null=True, verbose_name='Paused until'),
        ),
        migrations.AlterField(
            model_name='automationtaskmodel',
            name='locked',
            field=models.IntegerField(default=0, verbose_name='Locked'),
        ),
        migrations.AlterField(
            model_name='automationtaskmodel',
            name='message',
            field=models.CharField(blank=True, max_length=128, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='automationtaskmodel',
            name='previous',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='automations.automationtaskmodel', verbose_name='Previous task'),
        ),
        migrations.AlterField(
            model_name='automationtaskmodel',
            name='result',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Result'),
        ),
    ]
