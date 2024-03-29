# Generated by Django 2.1.7 on 2019-04-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190401_2213'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HealthCareLocations',
        ),
        migrations.AddField(
            model_name='search',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
