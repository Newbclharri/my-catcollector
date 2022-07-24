# Reference the Django docs if I get confused

from django.urls import path
from . import views

# Do not have to follow INDUCES pattern when using djange because
# Djange specifies the data type to look for 
# and will only select the route with the correct data type
# this is why route order doesn't matter in Django urls as opposed to routing in express JS
# Django routes also do not strictly follow RESTful routing as found in express JS
urlpatterns = [
    #This route maps to views.home Also, name='home' is a kwarg. Go research python kwargs
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats'),
    path('cats/<int:cat_id>', views.cats_detail, name='detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('photos/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup')
]