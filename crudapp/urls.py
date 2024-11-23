from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruits_table, name='fruits'),
    path('add/fruits', views.add_fruit, name='add-fruit'),
    path('delete/fruits/<int:pk>', views.delete_fruit, name='delete-fruit'),
    path('edit/fruits/<int:pk>', views.edit_fruit, name='edit-fruit'),
]