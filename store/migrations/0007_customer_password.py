# Generated by Django 4.0.1 on 2022-01-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=2, max_length=500),
            preserve_default=False,
        ),
    ]