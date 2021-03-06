# Generated by Django 4.0.5 on 2022-06-01 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_formaPago', models.IntegerField()),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento_Compra',
            fields=[
                ('id_seguimiento', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcripcion',
            fields=[
                ('num_sub', models.IntegerField(primary_key=True, serialize=False)),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('rut_vendedor', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('appaterno', models.CharField(max_length=50)),
                ('apmaterno', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('numero', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('num_venta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_formaPago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.forma_pago')),
                ('id_seguimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.seguimiento_compra')),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.cliente')),
                ('rut_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('imgen', models.ImageField(null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Estado_subcripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_sub', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.subcripcion')),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floreriaWeb.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('total', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.producto')),
                ('num_venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.venta')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floreriaWeb.region'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='floreriaWeb.comuna'),
        ),
    ]
