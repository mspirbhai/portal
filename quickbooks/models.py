from django.db import models
from organization.models import Organization

class QuickBooksSettings(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    sandbox_account = models.BooleanField(default=False)

    def __str__(self):
        return f"QuickBooks Settings for {self.organization}"



