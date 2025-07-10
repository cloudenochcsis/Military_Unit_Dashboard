from django.db import models
from django.utils import timezone

# Create your models here.

class Soldier(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Deployed', 'Deployed'),
    ]
    
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.rank} {self.name}"


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('Operational', 'Operational'),
        ('Maintenance', 'Maintenance'),
        ('Retired', 'Retired'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Operational')
    assigned_to = models.ForeignKey(Soldier, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.serial_number})"
