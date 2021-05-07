# Generated by Django 3.1.8 on 2021-05-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_automations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automationhookplugin',
            name='operation',
            field=models.IntegerField(choices=[(0, 'Automatisierung starten'), (1, 'Nachricht an Automatisierung')], default=1, verbose_name='Operation'),
        ),
        migrations.AlterField(
            model_name='automationhookplugin',
            name='automation',
            field=models.CharField(max_length=128, verbose_name='Automatisierung'),
        ),
        migrations.AlterField(
            model_name='automationhookplugin',
            name='token',
            field=models.CharField(blank=True, max_length=128, verbose_name='Optionales Token'),
        ),
        migrations.AlterField(
            model_name='automationstatusplugin',
            name='template',
            field=models.CharField(max_length=128, verbose_name='Daten der Aufgabe'),
        ),
    ]