from django.db import models

# Create your models here.
from users.models import Client, User, Worker


class Document(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = 'documents'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    assignee = models.ForeignKey(Worker, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.name


class Workflow(models.Model):
    status = models.IntegerField()  # add choices
    info = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    task = models.ForeignKey(Task, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'workflows'

    def __str__(self):
        return 'this is workflow'
