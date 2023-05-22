from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('register/', views.create_user, name='create_user'),
    path('update/<int:uid>/', views.update_user, name='update_user'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]