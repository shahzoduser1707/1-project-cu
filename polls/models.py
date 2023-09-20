from django.db import models

# Create your models here.

class BookModel(models.Model):
    name = models.CharField(default='',max_length=100)
    page = models.SmallIntegerField(default=1)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
