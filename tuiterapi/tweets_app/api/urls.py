from django.urls import path
from . import views

urlpatterns = [
    path('api/tuits/', views.find_tuits, name='find_tuits'),
    path('api/create/tuits/', views.create_tuit, name='create_tuit'),
    path('api/tuits/<int:tid>/', views.update_tuit, name='update_tuit'),
    path('api/tuits/delete/<int:tid>/', views.delete_tuit, name='delete_tuit'),
]
