# Generated by Django 3.2.2 on 2021-05-18 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimage_app', '0003_alter_image_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Image_data',
        ),
    ]