from django.contrib import admin
from .models import User, Project, Service, DailyTask, WorkEntry, Customer

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(DailyTask)
admin.site.register(WorkEntry)
admin.site.register(Customer)