from django.db import models

class Blood(models.Model):
    blood_type = models.CharField(max_length=120)
    description = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.blood_type
