from django.db import models
from django.contrib.auth.models import User

class Poost(models.Model):
    title = models.CharField(max_length=57)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
    