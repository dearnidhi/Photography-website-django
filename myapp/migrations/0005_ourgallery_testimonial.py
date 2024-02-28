# Generated by Django 5.0.1 on 2024-02-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_latestnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image', models.ImageField(upload_to='gallery_images/')),
                ('gallery_link', models.TextField()),
                ('gallery_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Our Gallery',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_image', models.ImageField(upload_to='testimonial_images/')),
                ('testimonial_heading', models.TextField()),
                ('testimonial_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]
