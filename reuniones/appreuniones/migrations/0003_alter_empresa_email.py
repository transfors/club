# Generated by Django 4.2.4 on 2023-08-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreuniones', '0002_alter_reunion_presentador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
