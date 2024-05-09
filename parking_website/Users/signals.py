import boto3
from django.conf import settings
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from .models import UsersProfile

client = boto3.client(
    's3',
    region_name = settings.AWS_S3_REGION_NAME,
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
)

@receiver(pre_save, sender=UsersProfile)
def delete_old_user_image(sender, instance,*args,**kwargs):
    print("Starting to delte old image")
    if not instance.pk:
        # Newly created
        return False
    
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False
    
    # Image is empty or default image
    if not old_instance.user_image or old_instance.user_image == settings.DEFAULT_PROFILE_IMAGE:
        return False
    
    new_image = instance.user_image
    if not old_instance.user_image == new_image:
        # Delete the old image
        old_image_path = old_instance.user_image
        client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=str(old_image_path))
        client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME_THUMBNAILS, Key=str(old_image_path))
    print("Delete successful")

