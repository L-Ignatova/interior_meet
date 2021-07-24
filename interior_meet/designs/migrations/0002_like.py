# Generated by Django 3.2.5 on 2021-07-24 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designs.design')),
            ],
        ),
    ]