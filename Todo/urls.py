from django.urls import path, include
from Todo import views

urlpatterns = [
    path('todolist/', views.UserTodoList.as_view(), name="todolist")
]
