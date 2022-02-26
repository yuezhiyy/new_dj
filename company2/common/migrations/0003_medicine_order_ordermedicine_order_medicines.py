# Generated by Django 4.0.1 on 2022-02-26 04:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_customer_qq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sn', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='medicines',
            field=models.ManyToManyField(through='common.OrderMedicine', to='common.Medicine'),
        ),
    ]
