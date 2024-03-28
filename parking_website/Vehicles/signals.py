import boto3
from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from .models import VehiclesVehicles

client = boto3.client(
    's3',
    region_name = settings.AWS_S3_REGION_NAME,
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
)

@receiver(pre_save, sender=VehiclesVehicles)
def delete_old_vehicle_image(sender, instance,*args,**kwargs):
    if not instance.pk:
        # Newly created
        return False
    
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False
    
    # Image is empty or default image
    if not old_instance.vehicle_image or old_instance.vehicle_image == settings.DEFAULT_VEHICLE_IMAGE:
        return False
    
    new_image = instance.vehicle_image
    if not old_instance.vehicle_image == new_image:
        # Delete the old image
        old_image_path = old_instance.vehicle_image
        client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=str(old_image_path))
        client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME_THUMBNAILS, Key=str(old_image_path))

