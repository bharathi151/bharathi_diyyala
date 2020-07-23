from django.db import models

class EmployeeTypes(models.TextChoices):
    MANAGER = "MANAGER"
    TECHNICIAN = "TECHNICIAN"
    DEVELOPER = "DEVELOPER"
    SALES_MEMBER = "SALES_MEMBER"
