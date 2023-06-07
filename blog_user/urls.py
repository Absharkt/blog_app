from django.urls import path
from . import views

urlpatterns = [
    path('base',views.index),
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('<str:frnd_id>',views.friend_blog,name='friend'),
]