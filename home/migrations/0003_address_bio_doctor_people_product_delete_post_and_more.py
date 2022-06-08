# Generated by Django 4.0.4 on 2022-06-08 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_post_surname_post_post_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people_title', models.CharField(max_length=10)),
                ('people_name', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
        migrations.AddField(
            model_name='bio',
            name='friends',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
    ]
