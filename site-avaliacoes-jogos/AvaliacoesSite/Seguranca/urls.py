from django.urls import path
from . import views

app_name = 'Seguranca'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('actual-logout/', views.actual_logout_view.as_view(), name='actual-logout'),
]