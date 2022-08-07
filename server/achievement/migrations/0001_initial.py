# Generated by Django 4.0.1 on 2022-08-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('success', models.IntegerField()),
                ('description', models.TextField()),
                ('count', models.IntegerField(null=0)),
            ],
        ),
    ]