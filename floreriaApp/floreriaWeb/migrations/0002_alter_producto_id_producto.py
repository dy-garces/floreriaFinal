# Generated by Django 4.0.5 on 2022-06-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreriaWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
