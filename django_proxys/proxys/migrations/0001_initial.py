# Generated by Django 4.0.2 on 2022-02-18 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=5)),
                ('protocol', models.CharField(max_length=5)),
                ('anonymity', models.CharField(default='None', max_length=4)),
                ('country', models.CharField(max_length=56)),
                ('region', models.CharField(max_length=56)),
                ('city', models.CharField(max_length=56)),
                ('uptime', models.DecimalField(decimal_places=2, max_digits=4)),
                ('response', models.IntegerField()),
                ('transfer', models.IntegerField()),
            ],
        ),
    ]