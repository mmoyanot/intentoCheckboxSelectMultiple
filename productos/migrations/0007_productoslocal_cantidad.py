# Generated by Django 2.0.7 on 2019-06-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20190606_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoslocal',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]