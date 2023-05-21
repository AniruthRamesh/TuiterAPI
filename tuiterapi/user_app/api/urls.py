from django.urls import path
from . import views

urlpatterns = [
    path('api/user/create', views.create_user, name='create_user'),
    path('api/user/update/<int:uid>', views.update_user, name='update_user'),
]