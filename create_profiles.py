import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiadomi_traderzy.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import UserProfile

for user in User.objects.all():
    UserProfile.objects.get_or_create(user=user) 