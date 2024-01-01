# Generated by Django 4.1.3 on 2022-12-17 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('country', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pays',
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('stock_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'produit',
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('invoice_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.pays')),
            ],
            options={
                'db_table': 'commande',
            },
        ),
        migrations.CreateModel(
            name='Details_commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField()),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.commande')),
                ('stock_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.produit')),
            ],
            options={
                'db_table': 'details_commande',
                'unique_together': {('invoice_no', 'stock_code')},
            },
        ),
    ]
