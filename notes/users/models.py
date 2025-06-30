from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="default_avatar.png", upload_to="profile_images")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    telephone = models.CharField(
        max_length=15, blank=True, validators=[RegexValidator(regex=r"^\+?1?\d{9,15}$")]
    )

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
