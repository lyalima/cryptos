# Generated by Django 5.1.3 on 2024-11-13 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('symbol', models.CharField(max_length=5, null=True)),
                ('price', models.FloatField(null=True)),
                ('moment', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
