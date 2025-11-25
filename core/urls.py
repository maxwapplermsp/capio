from rest_framework import routers
from .views import ProjectViewSet, ServiceViewSet, DailyTaskViewSet, WorkEntryViewSet, CustomerViewSet
from django.urls import path
from .views_frontend import index

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'dailytasks', DailyTaskViewSet)
router.register(r'workentries', WorkEntryViewSet)
router.register(r'customers', CustomerViewSet)

# Kombiniere API und Web-Routen:
urlpatterns = [
    path('', index, name='frontend-index'),    # <- Dies ist die neue Startseite!
] + router.urls