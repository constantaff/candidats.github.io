from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Elect(models.Model):
    name = models.CharField(verbose_name="Полное имя", max_length=400)
    votes = models.IntegerField(verbose_name="Количество голосов")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Избираемый"
        verbose_name_plural = "Избираемые"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(verbose_name="Уже проголосовал или нет", default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
