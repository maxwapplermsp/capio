from rest_framework import viewsets
from .models import Project, Service, DailyTask, WorkEntry, Customer
from .serializers import ProjectSerializer, ServiceSerializer, DailyTaskSerializer, WorkEntrySerializer, CustomerSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class DailyTaskViewSet(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer

class WorkEntryViewSet(viewsets.ModelViewSet):
    queryset = WorkEntry.objects.all()
    serializer_class = WorkEntrySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer