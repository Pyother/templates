# Generated by Django 4.2.dev20220708113012 on 2022-11-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_alter_system_border_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='basis',
            field=models.CharField(default='Wartość nominalna', max_length=100, verbose_name='Basis'),
        ),
    ]
