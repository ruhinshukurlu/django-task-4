# Generated by Django 3.0.7 on 2020-06-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(max_length=125)),
                ('picture', models.ImageField(upload_to='')),
                ('amount', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('production_date', models.DateTimeField()),
                ('is_new', models.BinaryField()),
                ('certificate', models.FileField(upload_to='')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('detailed_view_link', models.URLField()),
            ],
        ),
    ]
