# Generated by Django 4.2.dev20220708113012 on 2022-11-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_alter_system_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='feature_10',
            field=models.CharField(blank=True, default='Surname', max_length=100, verbose_name='Feature 10 (optional):'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_11',
            field=models.CharField(blank=True, default='rec@site.com', max_length=100, verbose_name='Feature 11 (optional):'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_9',
            field=models.CharField(blank=True, default='Name', max_length=100, verbose_name='Feature 9 (optional):'),
        ),
    ]
