# Generated by Django 4.0.1 on 2022-08-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='./image/default_image.jpg', upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('category', models.IntegerField()),
                ('style', models.IntegerField()),
                ('description', models.TextField()),
                ('soil', models.IntegerField(null=0)),
                ('air', models.IntegerField(null=0)),
                ('radio', models.IntegerField(null=0)),
                ('trash', models.IntegerField(null=0)),
                ('ocean', models.IntegerField(null=0)),
                ('approval', models.IntegerField(null=0)),
                ('capital', models.IntegerField(null=0)),
                ('product', models.IntegerField(null=0)),
            ],
        ),
    ]
