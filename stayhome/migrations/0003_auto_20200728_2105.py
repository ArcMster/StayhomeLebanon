# Generated by Django 3.0.2 on 2020-07-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stayhome', '0002_auto_20200728_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='android',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='iphone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
