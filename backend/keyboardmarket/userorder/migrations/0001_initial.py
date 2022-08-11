# Generated by Django 3.1.5 on 2022-07-31 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderno', models.CharField(max_length=255, verbose_name='訂單編號')),
                ('amount', models.IntegerField(verbose_name='商品數量')),
                ('status', models.IntegerField(verbose_name='狀態')),
                ('paypal_id', models.CharField(max_length=255, verbose_name='paypal訂單編號')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
