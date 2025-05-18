from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('o-nas/', views.AboutView.as_view(), name='about'),
    path('filmy/', views.VideosView.as_view(), name='videos'),
    path('szkolenia/', views.CoursesView.as_view(), name='courses'),
    path('platnosci/', views.PaymentView.as_view(), name='payment'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
] 