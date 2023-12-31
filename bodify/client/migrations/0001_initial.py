# Generated by Django 4.1.7 on 2023-10-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=50)),
                ('exercise1', models.CharField(default='', max_length=50)),
                ('desc1', models.CharField(max_length=500)),
                ('image1', models.ImageField(default='', upload_to='exercises/images')),
                ('exercise2', models.CharField(default='', max_length=50)),
                ('image2', models.ImageField(default='', upload_to='exercises/images')),
                ('desc2', models.CharField(max_length=500)),
                ('exercise3', models.IntegerField(default=0)),
                ('image3', models.ImageField(default='', upload_to='exercises/images')),
                ('desc3', models.CharField(max_length=500)),
            ],
        ),
    ]
