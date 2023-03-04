# Generated by Django 4.1.7 on 2023-03-04 01:52

from django.db import migrations, models
import users_pets_api.utils.path_utils


class Migration(migrations.Migration):

    dependencies = [
        ('users_pets_api', '0005_groups_and_roles_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='chip_number',
            field=models.CharField(db_column='chip_number', default='1111-2222-3333-4444', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(blank=True, null=True, upload_to=users_pets_api.utils.path_utils.get_pet_image_upload_path),
        ),
    ]