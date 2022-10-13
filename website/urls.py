from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('directors', views.directors, name='directors'),
    path('logout', views.logout_user, name='logout'),
    path('ratings', views.ratings, name='ratings'),
    path('rentals', views.rentals, name='rentals'),
]
