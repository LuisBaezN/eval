# Generated by Django 4.2.1 on 2023-07-21 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_productos_precio_alter_productos_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='pereced',
            new_name='perecedero',
        ),
    ]
