from django.urls import path
from . import views
from .apps import TodoConfig

app_name = TodoConfig.name

urlpatterns = [
    path("tasks/", views.TaskListView.as_view(), name="tasks_list"),
    path("tasks/new/", views.TaskCreateView.as_view(), name="task_create"),
    path(
        "task/<int:pk>/",
        views.TaskRetrieveUpdateDestroy.as_view(),
        name="task_view_edit_delete",
    ),
    path(
        "task/<int:pk>/complete/",
        views.TaskToggleComplete.as_view(),
        name="task_complete",
    ),
]
