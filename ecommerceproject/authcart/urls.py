
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('activate/',views.ActivateAccountView.as_view(),name='activate'),
]

#(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/





