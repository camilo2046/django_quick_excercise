# Generated by Django 4.1.7 on 2023-03-04 02:23

from django.db import migrations, models
import users_pets_api.utils.path_utils


class Migration(migrations.Migration):

    dependencies = [
        ('users_pets_api', '0006_pet_chip_number_pet_pet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_image',
            field=models.ImageField(blank=True, null=True, upload_to=users_pets_api.utils.path_utils.get_person_image_upload_path),
        ),
    ]