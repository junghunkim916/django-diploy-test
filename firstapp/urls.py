from . import views
from django.urls import path

app_name = 'firstapp'

urlpatterns = [
    path('signup',views.signup_view, name='signup'),
    path('list', views.listAPI, name= 'listAPI'),
    path('detail/<userId>', views.user_detail, name='userdetail')
]
