from django.db import models
# Create your models here.

class Test(models.Model):
    test_ad = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

