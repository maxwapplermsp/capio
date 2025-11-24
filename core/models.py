from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model (erweiterbar für Rollen, Fähigkeiten etc.)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teamlead', 'Teamleiter'),
        ('employee', 'Mitarbeiter'),
        ('hr', 'HR'),
        ('pm', 'Projektmanager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    skills = models.TextField(blank=True, null=True)
    availability = models.DecimalField(max_digits=5, decimal_places=2, default=40.0)  # z.B. Wochenstunden
    vacation_days = models.IntegerField(default=30)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    team = models.ManyToManyField(User, related_name='projects')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    weekly_effort_per_employee = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    team = models.ManyToManyField(User)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class DailyTask(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weekly_effort = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.user.username})'

class WorkEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    daily_task = models.ForeignKey(DailyTask, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    note = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.date}'