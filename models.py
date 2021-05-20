from django.db import models

# Create your models here.


class Forms(models.Model):
    name = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50, null=True)
    Phone_Number = models.IntegerField(null=True)
    Purpose = models.CharField(max_length=3000, null=True)

    def __str__(self):
        return self.name

