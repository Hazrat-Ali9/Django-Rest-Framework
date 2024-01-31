# Generated by Django 5.0.1 on 2024-01-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemsModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=3000)),
                ('category', models.CharField(choices=[('Books', 'Books'), ('Magazine', 'Magazine'), ('Movie', 'Movie')], max_length=30)),
                ('releaseDate', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='photos/products')),
            ],
        ),
    ]