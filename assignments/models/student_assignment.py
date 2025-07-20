from django.db import models
from assignments.models.base import BaseModel

class StudentAssignment(BaseModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("submitted", "Submitted"),
    ]

    student_name = models.CharField(max_length=100)
    assignment_title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.student_name} - {self.assignment_title}"
