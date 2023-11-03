# Generated by Django 4.2.7 on 2023-11-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='frequency',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
