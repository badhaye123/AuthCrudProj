# Generated by Django 3.2.6 on 2022-07-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(choices=[('Amazon', 'Amazon'), ('Flipkart', 'Flipkart'), ('Myntra', 'Myntra'), ('Ebay', 'Ebay'), ('Bigbasket', 'Bigbasket')], max_length=34)),
                ('product', models.CharField(choices=[('Clothes', 'Clothes'), ('Mobile', 'Mobile'), ('Laptop', 'Laptop'), ('Chair', 'Chair'), ('Grocery', 'Grocery')], max_length=34)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('is_paid', models.BooleanField()),
            ],
        ),
    ]
