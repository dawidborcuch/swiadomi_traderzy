from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    video_id = models.CharField(max_length=20, verbose_name="ID filmu", default="brak")
    thumbnail_url = models.URLField(verbose_name="URL miniatury", default="https://via.placeholder.com/320x180.png?text=Miniatura")
    published_at = models.DateTimeField(verbose_name="Data publikacji", default=timezone.now)
    is_training = models.BooleanField(default=False, verbose_name="Film szkoleniowy")
    is_premium = models.BooleanField(default=False, verbose_name="Film premium")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")

    class Meta:
        verbose_name = "Film YouTube"
        verbose_name_plural = "Filmy YouTube"
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class PaymentInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cena")
    currency = models.CharField(max_length=3, default="USD", verbose_name="Waluta")
    is_active = models.BooleanField(default=True, verbose_name="Aktywny")

    class Meta:
        verbose_name = "Informacja o płatności"
        verbose_name_plural = "Informacje o płatnościach"

    def __str__(self):
        return f"{self.title} - {self.price} {self.currency}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_premium_access = models.BooleanField(default=False)
    premium_access_until = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save() 