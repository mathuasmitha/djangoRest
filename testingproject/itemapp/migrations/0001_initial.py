# Generated by Django 4.0.8 on 2022-10-11 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Not Required', verbose_name='description')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 999.99'}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular_price')),
                ('discount', models.DecimalField(decimal_places=2, help_text='Maximum 999.99', max_digits=5, verbose_name='Discount_price')),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('stock', models.IntegerField()),
                ('imageUrl', models.URLField()),
                ('status', models.CharField(choices=[('AVL', 'Available'), ('NA', 'NotAvailable')], default='AVL', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='itemapp.category')),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
