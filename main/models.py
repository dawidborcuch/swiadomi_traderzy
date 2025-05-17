from django.db import models

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    video_url = models.URLField(verbose_name="Link do YouTube")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    is_training = models.BooleanField(default=False, verbose_name="Film szkoleniowy")

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