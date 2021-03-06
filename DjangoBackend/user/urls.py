from django.urls import path
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.views import LogoutView
from django.db import models
from function.models import PredData
from . import views
from user.views import PostListView

app_name = 'user'

urlpatterns = [
    # path('login', TemplateView.as_view(template_name='user/login.html'), name='login'),
    # path('agreement', TemplateView.as_view(template_name='user/agreement.html'), name='agreement'),
    path("detail/<int:pk>", DetailView.as_view(model=PredData, 
                                               template_name='user/detail.html'), 
                                               name='detail'),
    # path("mypage", views.PostListView.as_view(), name="mypage"), # list mypage로 연결
    path('mypage', PostListView.as_view(), name='mypage'),
    path('logout', LogoutView.as_view(), name='logout')
    ]
