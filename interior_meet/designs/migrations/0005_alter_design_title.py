# Generated by Django 3.2.5 on 2021-07-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0004_alter_design_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
