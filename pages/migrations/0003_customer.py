# Generated by Django 4.1.1 on 2022-10-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220922_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
