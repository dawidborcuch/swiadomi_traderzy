from django.contrib import admin
from .models import YouTubeVideo, PaymentInfo

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'is_training')
    list_filter = ('is_training', 'date_added')
    search_fields = ('title', 'description')

@admin.register(PaymentInfo)
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description') 