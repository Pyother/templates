# Generated by Django 4.2.dev20220708113012 on 2022-11-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_alter_candidate_feature_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='feature_10',
            field=models.CharField(default='Surname', max_length=100, verbose_name='Feature 10:'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_11',
            field=models.CharField(default='rec@site.com', max_length=100, verbose_name='Feature 11:'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_3',
            field=models.CharField(max_length=100, verbose_name='Feature 3:'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_4',
            field=models.CharField(max_length=100, verbose_name='Feature 4:'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_5',
            field=models.CharField(max_length=100, verbose_name='Feature 5:'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='feature_9',
            field=models.CharField(default='Name', max_length=100, verbose_name='Feature 9:'),
        ),
    ]