"""MDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from socius import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('index.html', v.index, name="index"),
    path('Python.html', v.Python, name="Python"),
    path('profile.html', v.profileView, name="profile"),
    path('profile', v.profileView, name="profile"),
    path('skills.html', v.skillsView, name="skills"),
    path('education.html', v.educationView, name="education"),
    path('certificate.html', v.certificateView, name="certificate"),
    path('testimonial.html', v.testimonialView, name="testimonial"),
    path('contactInfo.html', v.contactInfoView, name="conatactInfo"),
    path('address.html', v.addressView, name="address"),
    path('team.html', v.Team, name="team"),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('adduser/',v.simple_upload,name='simple_upload'),
    path('active/<uidb64>/<token>/',v.active, name='active'),
    
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

