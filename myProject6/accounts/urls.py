from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/upload/', permanent=False), name='home'),
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profile/', views.view_profile, name='view_profile'),
]
