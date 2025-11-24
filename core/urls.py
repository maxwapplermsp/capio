from rest_framework import routers
from .views import ProjectViewSet, ServiceViewSet, DailyTaskViewSet, WorkEntryViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'dailytasks', DailyTaskViewSet)
router.register(r'workentries', WorkEntryViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = router.urls