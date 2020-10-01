
from django.urls import path

from CRUD import admin
from . import  views

urlpatterns = [
 #  path('admin/', admin.site.urls),
    path('',views.index,name='index'),
  path('add_book/create/', views.create, name='create'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete/<id>/', views.delete, name='delete'),
     path('edit/<id>/', views.edit, name='edit'),
    path('edit/<id>/update', views.update, name='update'),


]
