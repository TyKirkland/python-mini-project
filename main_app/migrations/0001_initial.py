# Generated by Django 4.2.2 on 2023-07-06 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cephalopod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cephalopods', to='main_app.species')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='main_app.species')),
            ],
        ),
    ]
