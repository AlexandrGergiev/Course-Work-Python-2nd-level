# Generated by Django 4.0.2 on 2022-02-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Brand`s name')),
                ('summary', models.TextField(verbose_name='Summary of this brand')),
                ('producer', models.CharField(max_length=25, verbose_name='Country, brand produces in')),
            ],
        ),
    ]
