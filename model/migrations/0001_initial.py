# Generated by Django 4.2.1 on 2023-07-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descrip', models.TextField(max_length=200)),
                ('precio', models.PositiveSmallIntegerField()),
                ('cantidad', models.FloatField()),
                ('pereced', models.BooleanField()),
            ],
        ),
    ]
