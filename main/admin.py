from django.contrib import admin
from .models import YouTubeVideo, PaymentInfo, UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_premium_access', 'premium_access_until')
    list_filter = ('has_premium_access',)
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'premium_access_until'

@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_premium', 'is_training')
    list_filter = ('is_premium', 'is_training')
    search_fields = ('title', 'description')
    date_hierarchy = 'published_at'

@admin.register(PaymentInfo)
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'currency', 'is_active')
    list_filter = ('is_active', 'currency')
    search_fields = ('title', 'description') 