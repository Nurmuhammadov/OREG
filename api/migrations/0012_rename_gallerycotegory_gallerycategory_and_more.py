# Generated by Django 4.2.2 on 2023-07-17 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_gallery_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryCotegory',
            new_name='GalleryCategory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cotegory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='category/'),
        ),
    ]
