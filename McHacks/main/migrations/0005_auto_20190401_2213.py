# Generated by Django 2.1.7 on 2019-04-02 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_healthcarelocations'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcarelocations',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=12.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='healthcarelocations',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=12.0, max_digits=10),
            preserve_default=False,
        ),
    ]