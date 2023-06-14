from django.urls import path
from . import views

urlpatterns = [
    path('base',views.index),
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('friends/<int:frnd_id>',views.friend_blog,name='friend'),
    path('edit/<int:blog_id>',views.edit_blog,name='edit_blog'),

    path('send/<int:profile_id>', views.send_request, name='send_req'),
    path('accept/<int:profile_id>', views.accept_request, name='accept_req'),

    path('add-blog',views.add_blog,name='add_blog'),
    path('find-friends',views.find_friends,name='find_friends'),


]