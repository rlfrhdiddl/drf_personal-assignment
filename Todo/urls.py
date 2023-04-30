from django.urls import path, include
from Todo import views

urlpatterns = [
    path('todolist/', views.UserTodoList.as_view(), name="todolist"),
    path('showtodolist/', views.UserTodoList.as_view(), name="showtodolist"),
    path('deletetodolist/<int:pk>/',
         views.UserTodoList.as_view(), name="deletetodolist")
]
