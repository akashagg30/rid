# Generated by Django 5.0.6 on 2024-07-01 17:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organizations')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('handle', models.CharField(db_index=True, max_length=15, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('country_calling_code', models.CharField(blank=True, max_length=5, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_login_at', models.DateTimeField(blank=True, null=True)),
                ('initial_ip', models.CharField(blank=True, default=True, max_length=40, null=True)),
                ('last_ip', models.CharField(blank=True, default=True, max_length=40, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organizations')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.roles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]