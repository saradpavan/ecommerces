from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    
    
]

