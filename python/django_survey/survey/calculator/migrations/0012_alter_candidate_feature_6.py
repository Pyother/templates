# Generated by Django 4.2.dev20220708113012 on 2022-11-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0011_alter_candidate_feature_1_alter_candidate_feature_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='feature_6',
            field=models.CharField(max_length=100, verbose_name='Proponowane wynagrodzenie zasadnicze(PLN):'),
        ),
    ]