# Generated by Django 3.0.4 on 2020-04-06 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_ad', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
