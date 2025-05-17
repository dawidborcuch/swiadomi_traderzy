from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('o-nas/', views.AboutView.as_view(), name='about'),
    path('filmy/', views.VideosView.as_view(), name='videos'),
    path('szkolenia/', views.TrainingView.as_view(), name='training'),
    path('platnosci/', views.PaymentView.as_view(), name='payment'),
] 