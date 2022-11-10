from django.urls import path

from .views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    toggle_task_assign,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/toggle-assign/",
        toggle_task_assign,
        name="toggle-task-assign",
    ),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("tasks/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("tasks/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]

app_name = "task_manager"
