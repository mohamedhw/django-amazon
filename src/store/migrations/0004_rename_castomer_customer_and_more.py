# Generated by Django 4.0.4 on 2022-06-03 15:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_rename_images_product_image_alter_product_digital'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Castomer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='castomer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='castomer',
            new_name='customer',
        ),
    ]
