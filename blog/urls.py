from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPosts.as_view()),
    path('new_post/', views.CreatePost.as_view()),
    path('<slug>/', views.OnePost.as_view()),
    path('update/<slug>', views.EditPost.as_view()),
    path('delete/<slug>', views.DeletePost.as_view()),
]