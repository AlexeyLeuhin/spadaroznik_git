from django.db import models
from django.contrib.auth.models import User


class Publications(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    countries = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.countries
