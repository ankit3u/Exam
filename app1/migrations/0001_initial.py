# Generated by Django 4.1.1 on 2023-01-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
