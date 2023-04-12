from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.AllPosts.as_view()),
    path('new_post/', login_required(views.CreatePost.as_view())),
    path('<slug>/', views.OnePost.as_view(), name='one_post'),
    path('update/<slug>', views.EditPost.as_view(), name='update'),
    path('delete/<slug>', views.DeletePost.as_view(), name='delete'),
]