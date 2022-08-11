# Generated by Django 3.1.5 on 2022-07-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='商品名稱')),
                ('price', models.IntegerField(verbose_name='價格')),
                ('stored_amount', models.IntegerField(verbose_name='存量')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(verbose_name='狀態')),
                ('img', models.ImageField(upload_to='productImage/')),
                ('category', models.IntegerField(verbose_name='種類')),
                ('info', models.TextField(verbose_name='詳細描述')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]