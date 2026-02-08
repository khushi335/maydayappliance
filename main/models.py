from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
        
        
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)  # Added phone number
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class ServiceInquiry(models.Model):
    SERVICE_CHOICES = [
        ('Electrical Installation', 'Electrical Installation'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Maintenance & Repairs', 'Maintenance & Repairs'),
        ('Switchboard Upgrades', 'Switchboard Upgrades'),
        ('Lighting & Powerpoints', 'Lighting & Powerpoints'),
        ('Smoke Alarm Installation', 'Smoke Alarm Installation'),
        ('Safety Inspections', 'Safety Inspections'),
        ('Other Electrical Service', 'Other Electrical Service'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Service Inquiry"
        verbose_name_plural = "Service Inquiries"

    def __str__(self):
        return f"{self.name} - {self.service}"
        
class ScheduleContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"