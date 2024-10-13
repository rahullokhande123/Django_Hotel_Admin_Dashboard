# Generated by Django 5.1.2 on 2024-10-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_email', models.EmailField(max_length=254)),
                ('cust_query', models.TextField()),
            ],
        ),
    ]
