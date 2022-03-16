from django.urls import path, include
from . import views

app_name = 'Blog'
urlpatterns = [

    path('', views.home, name='home'),
    path('signup', views.signup_form, name='signup'),
    path('login', views.login_form, name='login'),
    path('logout', views.logout_form, name='logout'),
    path('daskboard', views.daskboard, name='daskboard'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('addpost', views.addPost, name='addpost'),
    path('updatepost/<int:id>', views.updatePost, name='updatepost'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost'),

]
