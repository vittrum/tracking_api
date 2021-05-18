import json

from rest_framework import views, generics, viewsets, status
# Create your views here.
from rest_framework.response import Response

from protection.models import Task
from users.models import Worker
from .serializers import TaskStatusSerializer, WorkerSerializer, TaskSerializer
from .services.encryptions import generate_private_key, sign_document


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerStartView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskStatusSerializer


class WorkerEndView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskStatusSerializer


class ClientApproveView(generics.UpdateAPIView):
    serializer_class = TaskStatusSerializer
    queryset = Task.objects.all()


class GetSignature(views.APIView):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        content = task.name
        key = generate_private_key()
        doc = sign_document(content, key)
        doc = json.dumps(doc)
        return Response(status=status.HTTP_200_OK, data=doc)
