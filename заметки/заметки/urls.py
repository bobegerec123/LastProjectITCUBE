from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('about', views.index),
    path('tips/add', views.add_tips),
    path('tips/delete/<id>', views.delete_tips),
    path('tips/edit/<id>', views.edit_tips),
    path('tips', views.tips_list),
]
