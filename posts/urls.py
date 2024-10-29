from django.urls import path, include
from .import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<int:id>', views.edit_post, name='edit_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),
    path('search/', views.search_blog, name='search_blog'),
]