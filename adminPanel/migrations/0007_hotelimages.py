# Generated by Django 3.2.11 on 2022-03-13 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0006_auto_20220312_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img7', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img8', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img9', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('img10', models.ImageField(blank=True, null=True, upload_to='hotel_images')),
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.hotels')),
            ],
        ),
    ]
