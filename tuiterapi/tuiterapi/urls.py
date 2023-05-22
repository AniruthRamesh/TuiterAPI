"""
URL configuration for TuiterAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from tweets_app.api import views as tweets_views
from user_app.api import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/tuits', tweets_views.create_tuit, name='create_tuit'),
    path('api/tuits', tweets_views.find_tuits, name='find_tuits'),
    path('api/tuits/<int:tid>', tweets_views.update_tuit, name='update_tuit'),
    path('api/tuits/delete/<int:tid>', tweets_views.delete_tuit, name='delete_tuit'),
    path('api/user/', include('user_app.api.urls')),
]


