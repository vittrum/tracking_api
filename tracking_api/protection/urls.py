from django.urls import path, include
from rest_framework import routers

from .views import GetSignature, TaskViewSet, WorkerViewSet, WorkerEndView, WorkerStartView, ClientApproveView

task_router = routers.SimpleRouter()
task_router.register('tasks', TaskViewSet)

worker_router = routers.SimpleRouter()
worker_router.register('worker', WorkerViewSet)

urlpatterns = [
    path('encrypt/', GetSignature.as_view()),
    path('worker-start/', WorkerStartView.as_view()),
    path('worker-end/', WorkerEndView.as_view()),
    path('client-approve/', ClientApproveView.as_view()),
]

urlpatterns += task_router.urls
urlpatterns += worker_router.urls



