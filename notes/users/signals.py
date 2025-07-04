from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


@receiver(post_save, sender=User)
def handle_user_profile(sender, instance, created, **kwargs):
    """
    Універсальний обробник для створення/оновлення профілю
    """
    Profile.objects.get_or_create(user=instance)
