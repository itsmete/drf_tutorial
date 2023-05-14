from django.urls import path
from . import views

urlpatterns = [
    path('',views.ForumListCreateAPIView.as_view(), name= 'home'),
    path('f/<str:pk>',views.ForumDetailAPIView.as_view(), name= 'forum-detail'),
]
