"""Whats4Dinner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
<<<<<<< HEAD
from API import views as api_views
=======
>>>>>>> 261b0ca88f8a1607c93cd7fbc25429cee781af15
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_views.home),
    path('about/', api_views.about),
    path('search/', api_views.search),
    path('signup/', api_views.signup),
    path('login/', api_views.user_login),
    path('updateProfile/', api_views.updateProfile),
    path('userprofile/', api_views.userprofile),
    path('logout/', api_views.user_logout),
<<<<<<< HEAD

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('create/', api_views.create),
    path('recipes/',api_views.recipe_details),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> 261b0ca88f8a1607c93cd7fbc25429cee781af15
