# Generated by Django 3.2.8 on 2021-10-08 03:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Address_book',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(max_length=255)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'interest',
                'unique_together': {('user_email', 'interests')},
            },
        ),
    ]
