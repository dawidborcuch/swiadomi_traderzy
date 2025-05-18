from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import YouTubeVideo, PaymentInfo, UserProfile
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

class CoursesView(ListView):
    model = YouTubeVideo
    template_name = 'main/training.html'
    context_object_name = 'videos'
    queryset = YouTubeVideo.objects.filter(is_training=True)

class PaymentView(ListView):
    model = PaymentInfo
    template_name = 'main/payment.html'
    context_object_name = 'payment_info'
    queryset = PaymentInfo.objects.filter(is_active=True)

def home(request):
    return render(request, 'main/home.html')

def videos(request):
    public_videos = YouTubeVideo.objects.filter(is_premium=False)
    premium_videos = YouTubeVideo.objects.filter(is_premium=True)
    has_premium = False
    
    print("\n=== DEBUG INFO ===")
    print(f"User authenticated: {request.user.is_authenticated}")
    if request.user.is_authenticated:
        print(f"Username: {request.user.username}")
        print(f"Has userprofile: {hasattr(request.user, 'userprofile')}")
        if hasattr(request.user, 'userprofile'):
            print(f"Premium access: {request.user.userprofile.has_premium_access}")
            has_premium = request.user.userprofile.has_premium_access
    print(f"Public videos count: {public_videos.count()}")
    print(f"Premium videos count: {premium_videos.count()}")
    print(f"Has premium (final): {has_premium}")
    print("=================\n")
    
    return render(request, 'main/videos.html', {
        'public_videos': public_videos,
        'premium_videos': premium_videos,
        'has_premium': has_premium,
    })

@login_required
def premium_videos(request):
    if not request.user.userprofile.has_premium_access:
        messages.error(request, 'Nie masz dostępu do tej sekcji.')
        return redirect('main:payment')
    videos = YouTubeVideo.objects.filter(is_premium=True)
    return render(request, 'main/premium_videos.html', {'videos': videos})

def courses(request):
    return render(request, 'main/courses.html')

def payment(request):
    return render(request, 'main/payment.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Zalogowano pomyślnie!')
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Konto zostało utworzone!')
            return redirect('main:home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Wylogowano pomyślnie.')
    return redirect('main:home') 