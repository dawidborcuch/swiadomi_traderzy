from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import YouTubeVideo, PaymentInfo
import requests

class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pobieranie danych o top 20 kryptowalutach
        try:
            response = requests.get('https://api.coingecko.com/api/v3/coins/markets',
                                 params={'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 20})
            context['crypto_data'] = response.json()
        except:
            context['crypto_data'] = []
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

class VideosView(ListView):
    model = YouTubeVideo
    template_name = 'main/videos.html'
    context_object_name = 'videos'
    queryset = YouTubeVideo.objects.filter(is_training=False)

class TrainingView(ListView):
    model = YouTubeVideo
    template_name = 'main/training.html'
    context_object_name = 'videos'
    queryset = YouTubeVideo.objects.filter(is_training=True)

class PaymentView(ListView):
    model = PaymentInfo
    template_name = 'main/payment.html'
    context_object_name = 'payment_info'
    queryset = PaymentInfo.objects.filter(is_active=True) 