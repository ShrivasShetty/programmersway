from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('feedback/',views.feedback),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.logout,name='logout'),
    path('pay/<str:flight_from>/<str:flight_to>',views.pay,name='pay'),
]